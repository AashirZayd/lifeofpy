from typing import List, Tuple
from pathlib import Path
from .base import FileSystemTransactionProtocol
from ..logging.logger import LoggerProtocol

class FileSystemTransaction(FileSystemTransactionProtocol):
    def __init__(self, service: 'FileSystemService', logger: LoggerProtocol):
        self.service = service
        self.logger = logger
        # Stores tuples of (backup_path, original_path) for rollback
        self.backups: List[Tuple[Path, Path]] = []
        # Stores paths that were created during the transaction (for cleanup on rollback)
        self.created: List[Path] = []
        self._committed = False

    def add_backup(self, backup_path: Path, original_path: Path) -> None:
        self.backups.append((backup_path, original_path))

    def add_created(self, path: Path) -> None:
        self.created.append(path)

    def commit(self) -> None:
        if self._committed:
            return
        self.logger.debug(f"Committing transaction with {len(self.backups)} backups and {len(self.created)} new paths")
        for backup_path, _ in self.backups:
            try:
                if backup_path.is_file():
                    backup_path.unlink(missing_ok=True)
                elif backup_path.is_dir():
                    import shutil
                    shutil.rmtree(backup_path, ignore_errors=True)
            except Exception as e:
                self.logger.warning(f"Failed to clean up backup {backup_path}: {e}")
        self._committed = True

    def rollback(self) -> None:
        if self._committed:
            self.logger.warning("Attempted to rollback a committed transaction")
            return
            
        self.logger.warning(f"Rolling back transaction. Restoring {len(self.backups)} files.")
        for backup_path, original_path in reversed(self.backups):
            try:
                self.service.restore(backup_path, original_path)
            except Exception as e:
                self.logger.critical(f"Failed to restore {original_path} from {backup_path}: {e}")
                
        for path in reversed(self.created):
            try:
                if path.exists():
                    self.logger.debug(f"Rolling back created path: {path}")
                    if path.is_file() or path.is_symlink():
                        path.unlink()
                    elif path.is_dir():
                        import shutil
                        shutil.rmtree(path)
            except Exception as e:
                self.logger.critical(f"Failed to cleanup created path {path}: {e}")
