from pathlib import Path
from core.filesystem.base import FileSystemProtocol
from .errors import CommitError

class CommitManager:
    def __init__(self, fs: FileSystemProtocol):
        self.fs = fs

    def commit_component(self, staged_dir: Path, target_dir: Path):
        try:
            if not self.fs.exists(target_dir):
                self.fs.create_directory(target_dir, parents=True)
            self.fs.copy(staged_dir, target_dir)
        except Exception as e:
            raise CommitError(f"Failed to commit component to {target_dir}: {e}")
