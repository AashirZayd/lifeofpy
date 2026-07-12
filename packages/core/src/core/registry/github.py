from typing import Optional
from pathlib import Path
from .base import RegistryProviderProtocol
from .models import Registry, ComponentManifest, PackManifest, RegistryMetadata
from .http import HttpClient
from .cache import RegistryCache
from .exceptions import RegistryUnavailableError, ComponentNotFoundError, ManifestNotFoundError
from ..logging.logger import LoggerProtocol
from ..filesystem.base import FileSystemProtocol

class GitHubProvider(RegistryProviderProtocol):
    def __init__(self, logger: LoggerProtocol, http: HttpClient, fs: FileSystemProtocol, cache: RegistryCache, base_url: str):
        self.logger = logger
        self.http = http
        self.fs = fs
        self.cache = cache
        self.base_url = base_url.rstrip('/')

    def _fetch_json(self, path: str) -> dict:
        url = f"{self.base_url}/{path}"
        cache_key = f"github_json_{path}"
        
        cached = self.cache.get(cache_key)
        if cached:
            return cached
            
        data = self.http.request_json(url)
        self.cache.set(cache_key, data)
        return data

    def get_registry(self) -> Registry:
        try:
            data = self._fetch_json("registry.json")
            return Registry.model_validate(data)
        except Exception as e:
            raise RegistryUnavailableError(f"Failed to fetch registry from GitHub: {e}")

    def get_manifest(self, slug: str) -> ComponentManifest:
        try:
            data = self._fetch_json(f"components/{slug}/manifest.json")
            return ComponentManifest.model_validate(data)
        except Exception as e:
            raise ManifestNotFoundError(f"Manifest for {slug} not found: {e}")

    def get_component(self, slug: str) -> ComponentManifest:
        return self.get_manifest(slug)

    def download_component(self, slug: str, dest_dir: Path) -> Path:
        self.logger.info(f"Downloading component {slug} to {dest_dir}")
        manifest = self.get_manifest(slug)
        
        if not self.fs.exists(dest_dir):
            self.fs.create_directory(dest_dir, parents=True)
            
        manifest_path = dest_dir / "manifest.json"
        self.fs.write_text_atomic(manifest_path, manifest.model_dump_json(indent=2))
        
        # Simplified file download list for Sprint 1
        files_to_download = ["component.py", "README.md"]
        
        for file in files_to_download:
            url = f"{self.base_url}/components/{slug}/{file}"
            try:
                content = self.http.request_bytes(url)
                file_path = dest_dir / file
                self.fs.write_bytes_atomic(file_path, content)
            except Exception as e:
                self.logger.warning(f"Failed to download optional file {file} for {slug}: {e}")
                
        return dest_dir

    def download_pack(self, slug: str, dest_dir: Path) -> Path:
        raise NotImplementedError("Packs are not supported yet")

    def component_exists(self, slug: str) -> bool:
        try:
            self.get_manifest(slug)
            return True
        except ManifestNotFoundError:
            return False

    def pack_exists(self, slug: str) -> bool:
        return False

    def health(self) -> bool:
        try:
            self._fetch_json("registry.json")
            return True
        except:
            return False

    def metadata(self) -> RegistryMetadata:
        reg = self.get_registry()
        return reg.metadata

    def version(self) -> str:
        reg = self.get_registry()
        return reg.version
