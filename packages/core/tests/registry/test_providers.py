import pytest
from pathlib import Path
from unittest.mock import MagicMock
from core.registry.models import Registry, RegistryMetadata, Checksum
from core.registry.github import GitHubProvider
from core.registry.local import LocalProvider
from core.registry.mirror import MirrorProvider
from core.registry.factory import RegistryFactory
from core.registry.exceptions import RegistryUnavailableError, ProviderConfigurationError
from core.logging.logger import DefaultLogger
from core.filesystem.service import FileSystemService

@pytest.fixture
def logger():
    return DefaultLogger(verbose=True)

@pytest.fixture
def fs(logger):
    return FileSystemService(logger)

def test_factory_creates_github_provider(logger, fs):
    factory = RegistryFactory(logger, fs)
    provider = factory.create_provider({"registry_url": "https://raw.githubusercontent.com/lifeofpy/registry/"})
    assert isinstance(provider, GitHubProvider)

def test_factory_creates_local_provider(logger, fs):
    factory = RegistryFactory(logger, fs)
    provider = factory.create_provider({"registry_url": "file:///tmp/registry"})
    assert isinstance(provider, LocalProvider)
    
def test_factory_invalid_url(logger, fs):
    factory = RegistryFactory(logger, fs)
    with pytest.raises(ProviderConfigurationError):
        factory.create_provider({"registry_url": "ftp://unsupported"})

def test_mirror_provider_failover(logger):
    mock_p1 = MagicMock()
    mock_p1.get_registry.side_effect = RegistryUnavailableError("Down")
    
    mock_p2 = MagicMock()
    mock_p2.get_registry.return_value = Registry(
        version="1.0.0",
        metadata=RegistryMetadata(
            registryVersion="1", schemaVersion="1", engineVersion="1",
            generatedAt="2026-01-01T00:00:00Z", componentCount=0,
            frameworkCount=0, categoryCount=0, checksum=Checksum(sha256="abc")
        ),
        components=[]
    )
    
    mirror = MirrorProvider(logger, [mock_p1, mock_p2])
    reg = mirror.get_registry()
    assert reg.version == "1.0.0"
    mock_p1.get_registry.assert_called_once()
    mock_p2.get_registry.assert_called_once()

def test_mirror_provider_all_fail(logger):
    mock_p1 = MagicMock()
    mock_p1.get_registry.side_effect = RegistryUnavailableError("Down")
    
    mirror = MirrorProvider(logger, [mock_p1])
    with pytest.raises(RegistryUnavailableError):
        mirror.get_registry()

def test_local_provider(logger, fs, tmp_path):
    reg_dir = tmp_path / "registry"
    fs.create_directory(reg_dir)
    
    reg_data = '{"version": "1.0.0", "metadata": {"registryVersion": "1", "schemaVersion": "1", "engineVersion": "1", "generatedAt": "2026-01-01T00:00:00Z", "componentCount": 0, "frameworkCount": 0, "categoryCount": 0, "checksum": {"sha256": "abc"}}, "components": []}'
    fs.write_text_atomic(reg_dir / "registry.json", reg_data)
    
    provider = LocalProvider(logger, fs, reg_dir)
    assert provider.health() is True
    
    reg = provider.get_registry()
    assert reg.version == "1.0.0"
