from pathlib import Path

import pytest
from core.filesystem.service import FileSystemService
from core.logging.logger import DefaultLogger
from engine.dependency_graph.models import InstallPlan, InstallPlanStage
from engine.downloader.models import DownloadResult
from engine.installer.errors import InstallError
from engine.installer.service import InstallerService


class MockDownloader:
    def download(self, component_slug: str, version: str) -> DownloadResult:
        if component_slug == "fail_download":
            return DownloadResult(
                id="123",
                component_slug=component_slug,
                staged_path="",
                bytes_downloaded=0,
                success=False,
                error_message="Network error",
            )
        return DownloadResult(
            id="123",
            component_slug=component_slug,
            staged_path=f"/tmp/staged/{component_slug}",
            bytes_downloaded=100,
            success=True,
        )


class MockValidator:
    def validate_component(self, path: Path):
        class MockReport:
            has_errors = False

            def get_errors(self):
                return []

        if "fail_verify" in str(path):

            class FailedReport:
                has_errors = True

                def get_errors(self):
                    class Err:
                        description = "Bad manifest"

                    return [Err()]

            return FailedReport()

        return MockReport()


@pytest.fixture
def logger():
    return DefaultLogger()


@pytest.fixture
def fs(logger, tmp_path):
    class MockFS(FileSystemService):
        def exists(self, path: Path) -> bool:
            if ".lifeofpy.lock.pid" in str(path):
                return False
            return True

        def create_directory(self, path: Path, parents: bool = False):
            pass

        def copy(self, src: Path, dest: Path):
            pass

        def write_text_atomic(self, path: Path, content: str):
            pass

        def delete_file(self, path: Path):
            pass

        def delete_directory(self, path: Path, recursive: bool = False):
            pass

        def read_text(self, path: Path):
            if "history" in str(path):
                return '{"entries": []}'
            return "{}"

    return MockFS(logger)


@pytest.fixture
def service(logger, fs):
    downloader = MockDownloader()
    validator = MockValidator()
    return InstallerService(logger, fs, downloader, validator)


def test_successful_installation(service, tmp_path):
    plan = InstallPlan(total_components=1, stages=[InstallPlanStage(name="Download", components=["button"])])

    events = []
    service.subscribe(lambda e: events.append(e.name))

    service.install(plan, tmp_path)

    assert "InstallationStarted" in events
    assert "ComponentInstalling" in events
    assert "ComponentInstalled" in events
    assert "InstallationCompleted" in events
    assert "RollbackStarted" not in events


def test_download_failure_triggers_rollback(service, tmp_path):
    plan = InstallPlan(total_components=1, stages=[InstallPlanStage(name="Download", components=["fail_download"])])

    events = []
    service.subscribe(lambda e: events.append(e.name))

    with pytest.raises(InstallError):
        service.install(plan, tmp_path)

    assert "RollbackStarted" in events
    assert "RollbackCompleted" in events


def test_verification_failure_triggers_rollback(service, tmp_path):
    plan = InstallPlan(total_components=1, stages=[InstallPlanStage(name="Download", components=["fail_verify"])])

    events = []
    service.subscribe(lambda e: events.append(e.name))

    with pytest.raises(InstallError):
        service.install(plan, tmp_path)

    assert "RollbackStarted" in events
