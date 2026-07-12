from pathlib import Path
from core.filesystem.base import FileSystemProtocol
from .errors import ProjectLockedError, TransactionError

class TransactionManager:
    def __init__(self, fs: FileSystemProtocol):
        self.fs = fs

    def acquire_lock(self, project_dir: Path):
        lock_file = project_dir / ".lifeofpy.lock.pid"
        if self.fs.exists(lock_file):
            raise ProjectLockedError(f"Project is already locked at {lock_file}. Another installer might be running.")
        try:
            self.fs.write_text_atomic(lock_file, "LOCKED")
        except Exception as e:
            raise TransactionError(f"Failed to acquire project lock: {e}")

    def release_lock(self, project_dir: Path):
        lock_file = project_dir / ".lifeofpy.lock.pid"
        if self.fs.exists(lock_file):
            try:
                self.fs.delete_file(lock_file)
            except Exception as e:
                raise TransactionError(f"Failed to release project lock: {e}")
