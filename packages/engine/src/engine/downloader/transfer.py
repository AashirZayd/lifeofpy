from pathlib import Path

from core.filesystem.base import FileSystemProtocol
from core.registry.base import RegistryProviderProtocol

from .errors import NetworkFailureError


class TransferEngine:
    def __init__(self, provider: RegistryProviderProtocol, fs: FileSystemProtocol):
        self.provider = provider
        self.fs = fs

    def download_component(self, component_slug: str, version: str, destination_dir: Path) -> int:
        try:
            self.provider.download_component(component_slug, destination_dir)

            total_bytes = 0
            for f in destination_dir.rglob("*"):
                if f.is_file():
                    total_bytes += len(self.fs.read_bytes(f))
            return total_bytes
        except Exception as e:
            raise NetworkFailureError(f"Failed to transfer {component_slug}: {e}") from e
