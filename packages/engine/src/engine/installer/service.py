from pathlib import Path

from core.filesystem.base import FileSystemProtocol
from core.logging.logger import LoggerProtocol

from engine.dependency_graph.models import InstallPlan
from engine.downloader.service import DownloaderService
from engine.validator.service import ManifestValidationService

from .events import EventBus
from .executor import InstallExecutor
from .history import HistoryManager
from .rollback import RollbackManager
from .types import EventCallback
from .verification import InstallationVerifier


class InstallerService:
    def __init__(
        self,
        logger: LoggerProtocol,
        fs: FileSystemProtocol,
        downloader: DownloaderService,
        validator: ManifestValidationService,
    ):
        self.logger = logger
        self.fs = fs
        self.bus = EventBus(logger)
        self.verifier = InstallationVerifier(fs, validator)
        self.executor = InstallExecutor(logger, fs, downloader, self.verifier, self.bus)
        self.history_mgr = HistoryManager(fs)
        self.rollback_mgr = RollbackManager(fs)

    def subscribe(self, callback: EventCallback):
        self.bus.subscribe(callback)

    def install(self, plan: InstallPlan, project_dir: Path | str):
        self.executor.execute(plan, Path(project_dir))

    def uninstall(self, component_slug: str, project_dir: Path | str):
        target_dir = Path(project_dir) / "components" / component_slug
        self.rollback_mgr.rollback_component(target_dir)

    def verify(self, component_slug: str, project_dir: Path | str) -> bool:
        return self.verifier.verify_installation(Path(project_dir), component_slug)

    def rollback(self, component_slug: str, project_dir: Path | str):
        self.uninstall(component_slug, project_dir)

    def history(self, project_dir: Path | str) -> dict:
        history_file = Path(project_dir) / ".lifeofpy" / "history.json"
        if self.fs.exists(history_file):
            import json

            return json.loads(self.fs.read_text(history_file))
        return {}

    def status(self) -> dict:
        return {"status": "idle"}
