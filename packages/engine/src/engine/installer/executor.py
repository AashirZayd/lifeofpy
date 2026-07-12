from pathlib import Path

from core.filesystem.base import FileSystemProtocol
from core.logging.logger import LoggerProtocol

from engine.dependency_graph.models import InstallPlan
from engine.downloader.service import DownloaderService

from .commit import CommitManager
from .errors import InstallError
from .events import EventBus
from .history import HistoryManager
from .lockfile import LockfileManager
from .models import InstallEvent
from .rollback import RollbackManager
from .transactions import TransactionManager
from .verification import InstallationVerifier
from .workspace import WorkspaceManager


class InstallExecutor:
    def __init__(
        self,
        logger: LoggerProtocol,
        fs: FileSystemProtocol,
        downloader: DownloaderService,
        verifier: InstallationVerifier,
        bus: EventBus,
    ):
        self.logger = logger
        self.fs = fs
        self.downloader = downloader
        self.verifier = verifier
        self.bus = bus
        self.workspace = WorkspaceManager(fs)
        self.tx = TransactionManager(fs)
        self.commit = CommitManager(fs)
        self.rollback = RollbackManager(fs)
        self.history = HistoryManager(fs)
        self.lockfile = LockfileManager(fs)

    def execute(self, plan: InstallPlan, project_dir: Path):
        self.bus.emit(InstallEvent(name="InstallationStarted"))
        self.tx.acquire_lock(project_dir)
        workspace_dir = self.workspace.create_workspace(project_dir)

        installed_slugs = []

        try:
            download_stage = next((s for s in plan.stages if s.name == "Download"), None)
            if not download_stage:
                raise InstallError("Invalid InstallPlan: Missing Download stage.")

            for component_slug in download_stage.components:
                self.bus.emit(InstallEvent(name="ComponentInstalling", component_slug=component_slug))

                result = self.downloader.download(component_slug, "latest")
                if not result.success:
                    raise InstallError(f"Failed to download {component_slug}: {result.error_message}")

                staged_dir = Path(result.staged_path)

                self.bus.emit(InstallEvent(name="VerificationStarted", component_slug=component_slug))
                self.verifier.verify_staged_component(staged_dir)
                self.bus.emit(InstallEvent(name="VerificationCompleted", component_slug=component_slug))

                target_dir = project_dir / "components" / component_slug
                self.commit.commit_component(staged_dir, target_dir)
                installed_slugs.append(component_slug)

                self.verifier.verify_installation(project_dir, component_slug)

                self.history.record_install(project_dir, component_slug, "1.0.0")
                self.lockfile.update_lockfile(project_dir, component_slug, "1.0.0", [], "checksum_stub")

                self.bus.emit(InstallEvent(name="ComponentInstalled", component_slug=component_slug))

        except Exception as e:
            self.bus.emit(InstallEvent(name="RollbackStarted", message=str(e)))
            self.logger.error(f"Installation failed: {e}. Rolling back.")
            for slug in installed_slugs:
                target_dir = project_dir / "components" / slug
                self.rollback.rollback_component(target_dir)
            self.bus.emit(InstallEvent(name="RollbackCompleted"))
            raise InstallError(f"Installation aborted and rolled back: {e}") from e

        finally:
            self.workspace.cleanup_workspace(workspace_dir)
            self.tx.release_lock(project_dir)
            self.bus.emit(InstallEvent(name="InstallationCompleted"))
