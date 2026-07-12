import pytest
from pathlib import Path
from core.filesystem.service import FileSystemService
from core.logging.logger import DefaultLogger
from core.registry.base import RegistryProviderProtocol
from engine.downloader.service import DownloaderService
from engine.downloader.errors import ChecksumMismatchError, NetworkFailureError

class MockProvider(RegistryProviderProtocol):
    def get_manifest(self, component_slug: str, version: str = "latest"):
        return {"id": component_slug, "slug": component_slug}
        
    def download_component(self, component_slug: str, destination_dir: Path, version: str = "latest"):
        if component_slug == "fail_network":
            raise Exception("Mock network failure")
            
        manifest_file = destination_dir / "manifest.json"
        with open(manifest_file, "w") as f:
            f.write('{"id": "test"}')
            
    def metadata(self):
        return {}

@pytest.fixture
def logger():
    return DefaultLogger()

@pytest.fixture
def fs(logger):
    return FileSystemService(logger)

@pytest.fixture
def provider():
    return MockProvider()

@pytest.fixture
def service(provider, fs, logger):
    return DownloaderService(provider, fs, logger)

def test_successful_download(service, fs):
    result = service.download("button", "latest")
    assert result.success
    assert "button" in result.staged_path
    assert fs.exists(Path(result.staged_path) / "manifest.json")

def test_network_failure(service):
    result = service.download("fail_network", "latest")
    assert not result.success
    assert "Mock network failure" in result.error_message
    
def test_checksum_mismatch(service, fs):
    result = service.download("button", "latest", expected_checksum="invalid_checksum")
    assert not result.success
    assert "Checksum mismatch" in result.error_message

def test_batch_download(service):
    results = service.download_batch([
        {"slug": "btn-1"},
        {"slug": "btn-2"}
    ])
    assert len(results) == 2
    assert results[0].success
    assert results[1].success
    
def test_metrics(service):
    service.download("btn", "latest")
    service.download("fail_network", "latest")
    
    stats = service.status()
    assert stats["total_downloads"] == 2
    assert stats["failed_downloads"] == 1
