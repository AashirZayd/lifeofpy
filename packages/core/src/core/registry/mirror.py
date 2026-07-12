from typing import List, Optional
from pathlib import Path
from .base import RegistryProviderProtocol
from .models import Registry, ComponentManifest, RegistryMetadata
from .exceptions import RegistryUnavailableError, ComponentNotFoundError
from ..logging.logger import LoggerProtocol

class MirrorProvider(RegistryProviderProtocol):
    """A provider that attempts multiple backend providers in sequence (Failover)."""
    def __init__(self, logger: LoggerProtocol, providers: List[RegistryProviderProtocol]):
        if not providers:
            raise ValueError("MirrorProvider requires at least one backend provider")
        self.logger = logger
        self.providers = providers

    def _execute_with_failover(self, func_name: str, *args, **kwargs):
        last_exception = None
        for i, provider in enumerate(self.providers):
            try:
                self.logger.debug(f"Mirror attempting {func_name} on provider {i+1}/{len(self.providers)}")
                func = getattr(provider, func_name)
                return func(*args, **kwargs)
            except Exception as e:
                self.logger.warning(f"Mirror provider {i+1} failed for {func_name}: {e}")
                last_exception = e
                
        raise RegistryUnavailableError(f"All mirror providers failed for {func_name}. Last error: {last_exception}")

    def get_registry(self) -> Registry:
        return self._execute_with_failover("get_registry")

    def get_manifest(self, slug: str) -> ComponentManifest:
        return self._execute_with_failover("get_manifest", slug)

    def get_component(self, slug: str) -> ComponentManifest:
        return self._execute_with_failover("get_component", slug)

    def download_component(self, slug: str, dest_dir: Path) -> Path:
        return self._execute_with_failover("download_component", slug, dest_dir)

    def download_pack(self, slug: str, dest_dir: Path) -> Path:
        return self._execute_with_failover("download_pack", slug, dest_dir)

    def component_exists(self, slug: str) -> bool:
        for provider in self.providers:
            if getattr(provider, "health")() and getattr(provider, "component_exists")(slug):
                return True
        return False

    def pack_exists(self, slug: str) -> bool:
        return False

    def health(self) -> bool:
        return any(p.health() for p in self.providers)

    def metadata(self) -> RegistryMetadata:
        return self._execute_with_failover("metadata")

    def version(self) -> str:
        return self._execute_with_failover("version")
