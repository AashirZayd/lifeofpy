import os
from pathlib import Path
from .base import RegistryProviderProtocol
from .github import GitHubProvider
from .local import LocalProvider
from .mirror import MirrorProvider
from .http import HttpClient
from .cache import RegistryCache
from ..logging.logger import LoggerProtocol
from ..filesystem.base import FileSystemProtocol
from .exceptions import ProviderConfigurationError

class RegistryFactory:
    def __init__(self, logger: LoggerProtocol, fs: FileSystemProtocol):
        self.logger = logger
        self.fs = fs

    def create_provider(self, config: dict) -> RegistryProviderProtocol:
        """
        Creates the appropriate provider based on the configuration hierarchy.
        config should be resolved beforehand (CLI > ENV > JSON).
        """
        registry_url = config.get("registry_url")
        if not registry_url:
            registry_url = os.getenv("LIFEOFPY_REGISTRY", "https://raw.githubusercontent.com/lifeofpy/registry/main/registry/v1/")

        self.logger.info(f"Instantiating registry provider for: {registry_url}")

        if registry_url.startswith("http://") or registry_url.startswith("https://"):
            http = HttpClient(self.logger)
            cache_dir = Path.home() / ".lifeofpy" / "cache" / "registry"
            cache = RegistryCache(self.fs, self.logger, cache_dir)
            return GitHubProvider(self.logger, http, self.fs, cache, registry_url)
            
        elif registry_url.startswith("file://") or registry_url.startswith("/") or registry_url.startswith("C:\\") or registry_url.startswith("D:\\"):
            path_str = registry_url.replace("file://", "")
            return LocalProvider(self.logger, self.fs, Path(path_str))
            
        else:
            raise ProviderConfigurationError(f"Unsupported registry URL format: {registry_url}")
            
    def create_mirror(self, configs: list[dict]) -> RegistryProviderProtocol:
        providers = [self.create_provider(cfg) for cfg in configs]
        return MirrorProvider(self.logger, providers)
