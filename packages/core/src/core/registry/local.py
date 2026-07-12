from typing import Optional
from pathlib import Path
import json
from .base import RegistryProviderProtocol
from .models import Registry, ComponentManifest, PackManifest, RegistryMetadata
from .exceptions import RegistryUnavailableError, ComponentNotFoundError, ManifestNotFoundError
from ..logging.logger import LoggerProtocol
from ..filesystem.base import FileSystemProtocol

class LocalProvider(RegistryProviderProtocol):
    def __init__(self, logger: LoggerProtocol, fs: FileSystemProtocol, registry_dir: Path):
        self.logger = logger
        self.fs = fs
        self.registry_dir = registry_dir

    def _read_json(self, path: str) -> dict:
        full_path = self.registry_dir / path
        if not self.fs.exists(full_path):
            raise FileNotFoundError(f"Not found: {full_path}")
        content = self.fs.read_text(full_path)
        return json.loads(content)

    def get_registry(self) -> Registry:
        try:
            data = self._read_json("registry.json")
            return Registry.model_validate(data)
        except Exception as e:
            raise RegistryUnavailableError(f"Failed to read local registry: {e}")

    def get_manifest(self, slug: str) -> ComponentManifest:
        try:
            data = self._read_json(f"components/{slug}/manifest.json")
            return ComponentManifest.model_validate(data)
        except Exception as e:
            raise ManifestNotFoundError(f"Local manifest for {slug} not found: {e}")

    def get_component(self, slug: str) -> ComponentManifest:
        return self.get_manifest(slug)

    def download_component(self, slug: str, dest_dir: Path) -> Path:
        self.logger.info(f"Copying component {slug} locally to {dest_dir}")
        src_dir = self.registry_dir / "components" / slug
        
        if not self.fs.exists(src_dir):
            raise ComponentNotFoundError(f"Component source not found at {src_dir}")
            
        if not self.fs.exists(dest_dir):
            self.fs.create_directory(dest_dir, parents=True)
            
        with self.fs.transaction() as tx:
            self.fs.copy(src_dir, dest_dir)
            
        return dest_dir

    def download_pack(self, slug: str, dest_dir: Path) -> Path:
        raise NotImplementedError("Packs are not supported yet")

    def component_exists(self, slug: str) -> bool:
        return self.fs.exists(self.registry_dir / "components" / slug / "manifest.json")

    def pack_exists(self, slug: str) -> bool:
        return False

    def health(self) -> bool:
        return self.fs.exists(self.registry_dir / "registry.json")

    def metadata(self) -> RegistryMetadata:
        return self.get_registry().metadata

    def version(self) -> str:
        return self.get_registry().version
