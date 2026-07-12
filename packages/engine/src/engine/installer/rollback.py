from pathlib import Path
from core.filesystem.base import FileSystemProtocol
from .errors import RollbackError

class RollbackManager:
    def __init__(self, fs: FileSystemProtocol):
        self.fs = fs

    def rollback_component(self, target_dir: Path):
        try:
            if self.fs.exists(target_dir):
                self.fs.delete_directory(target_dir, recursive=True)
        except Exception as e:
            raise RollbackError(f"Failed to rollback component at {target_dir}: {e}")
