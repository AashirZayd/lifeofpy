import os
import tempfile
import shutil
from pathlib import Path
from contextlib import contextmanager
from typing import Iterator

from .base import FileSystemProtocol
from .transactions import FileSystemTransaction
from ..exceptions.filesystem import (
    PathNotFoundError, PermissionDeniedError, AtomicWriteError,
    BackupError, RollbackError, InvalidPathError, FilesystemError
)
from ..logging.logger import LoggerProtocol

class FileSystemService(FileSystemProtocol):
    def __init__(self, logger: LoggerProtocol):
        self.logger = logger
        self._current_tx: FileSystemTransaction | None = None

    def _get_path(self, path: Path | str) -> Path:
        return Path(path).resolve()

    def exists(self, path: Path | str) -> bool:
        return self._get_path(path).exists()

    def read_text(self, path: Path | str) -> str:
        p = self._get_path(path)
        if not p.exists():
            raise PathNotFoundError(f"File not found: {p}")
        try:
            return p.read_text(encoding='utf-8')
        except PermissionError:
            raise PermissionDeniedError(f"Permission denied: {p}")

    def read_bytes(self, path: Path | str) -> bytes:
        p = self._get_path(path)
        if not p.exists():
            raise PathNotFoundError(f"File not found: {p}")
        try:
            return p.read_bytes()
        except PermissionError:
            raise PermissionDeniedError(f"Permission denied: {p}")

    def backup(self, path: Path | str) -> Path:
        p = self._get_path(path)
        if not p.exists():
            raise PathNotFoundError(f"Cannot backup missing path: {p}")
        
        backup_dir = Path(tempfile.mkdtemp(prefix="lifeofpy_backup_"))
        backup_path = backup_dir / p.name
        
        try:
            if p.is_dir():
                shutil.copytree(p, backup_path, dirs_exist_ok=True)
            else:
                shutil.copy2(p, backup_path)
            self.logger.debug(f"Created backup of {p} at {backup_path}")
            return backup_path
        except Exception as e:
            raise BackupError(f"Failed to backup {p}: {e}")

    def restore(self, backup_path: Path | str, original_path: Path | str) -> None:
        bp = self._get_path(backup_path)
        op = self._get_path(original_path)
        
        self.logger.info(f"Restoring {op} from {bp}")
        try:
            if op.exists():
                if op.is_dir():
                    shutil.rmtree(op)
                else:
                    op.unlink()
                    
            if bp.is_dir():
                shutil.copytree(bp, op, dirs_exist_ok=True)
            else:
                shutil.copy2(bp, op)
        except Exception as e:
            raise RollbackError(f"Failed to restore {op}: {e}")

    def write_text_atomic(self, path: Path | str, content: str) -> None:
        self.write_bytes_atomic(path, content.encode('utf-8'))

    def write_bytes_atomic(self, path: Path | str, content: bytes) -> None:
        p = self._get_path(path)
        
        if self._current_tx and p.exists():
            backup_path = self.backup(p)
            self._current_tx.add_backup(backup_path, p)
        elif self._current_tx and not p.exists():
            self._current_tx.add_created(p)

        parent = p.parent
        parent.mkdir(parents=True, exist_ok=True)
        
        temp_fd, temp_path_str = tempfile.mkstemp(dir=parent, prefix=".tmp_")
        temp_path = Path(temp_path_str)
        
        try:
            with os.fdopen(temp_fd, 'wb') as f:
                f.write(content)
            os.replace(temp_path, p)
            self.logger.debug(f"Atomically wrote {len(content)} bytes to {p}")
        except Exception as e:
            if temp_path.exists():
                temp_path.unlink(missing_ok=True)
            raise AtomicWriteError(f"Atomic write failed for {p}: {e}")

    def copy(self, src: Path | str, dst: Path | str) -> None:
        s = self._get_path(src)
        d = self._get_path(dst)
        
        if not s.exists():
            raise PathNotFoundError(f"Source not found: {s}")
            
        if self._current_tx and d.exists():
            backup_path = self.backup(d)
            self._current_tx.add_backup(backup_path, d)
        elif self._current_tx and not d.exists():
            self._current_tx.add_created(d)
            
        try:
            if s.is_dir():
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
            self.logger.debug(f"Copied {s} to {d}")
        except Exception as e:
            raise FilesystemError(f"Failed to copy {s} to {d}: {e}")

    def move(self, src: Path | str, dst: Path | str) -> None:
        s = self._get_path(src)
        d = self._get_path(dst)
        
        if not s.exists():
            raise PathNotFoundError(f"Source not found: {s}")
            
        if self._current_tx and d.exists():
            backup_path = self.backup(d)
            self._current_tx.add_backup(backup_path, d)
        elif self._current_tx and not d.exists():
            self._current_tx.add_created(d)
            
        try:
            if self._current_tx:
                self.copy(s, d)
                self.delete(s)
            else:
                shutil.move(s, d)
            self.logger.debug(f"Moved {s} to {d}")
        except Exception as e:
            raise FilesystemError(f"Failed to move {s} to {d}: {e}")

    def delete(self, path: Path | str) -> None:
        p = self._get_path(path)
        if not p.exists():
            return
            
        if self._current_tx:
            backup_path = self.backup(p)
            self._current_tx.add_backup(backup_path, p)
            
        try:
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()
            self.logger.debug(f"Deleted {p}")
        except Exception as e:
            raise FilesystemError(f"Failed to delete {p}: {e}")

    def rename(self, src: Path | str, dst: Path | str) -> None:
        self.move(src, dst)

    def create_directory(self, path: Path | str, parents: bool = True) -> None:
        p = self._get_path(path)
        if p.exists():
            return
            
        try:
            p.mkdir(parents=parents, exist_ok=True)
            if self._current_tx:
                self._current_tx.add_created(p)
            self.logger.debug(f"Created directory {p}")
        except Exception as e:
            raise FilesystemError(f"Failed to create directory {p}: {e}")

    def delete_directory(self, path: Path | str, recursive: bool = False) -> None:
        p = self._get_path(path)
        if not p.exists():
            return
        if not p.is_dir():
            raise InvalidPathError(f"Not a directory: {p}")
            
        if not recursive and any(p.iterdir()):
            raise FilesystemError(f"Directory not empty: {p}")
            
        self.delete(p)

    def is_symlink(self, path: Path | str) -> bool:
        return Path(path).is_symlink()

    @contextmanager
    def transaction(self) -> Iterator[FileSystemTransaction]:
        if self._current_tx is not None:
            yield self._current_tx
            return
            
        tx = FileSystemTransaction(self, self.logger)
        self._current_tx = tx
        self.logger.info("Beginning filesystem transaction")
        
        try:
            yield tx
            tx.commit()
        except Exception as e:
            self.logger.error(f"Transaction failed, triggering rollback: {e}")
            tx.rollback()
            raise
        finally:
            self._current_tx = None
