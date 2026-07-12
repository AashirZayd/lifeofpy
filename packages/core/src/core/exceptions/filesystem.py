from .base import LifeOfPyError

class FilesystemError(LifeOfPyError):
    """Base class for all filesystem related errors."""
    pass

class PathNotFoundError(FilesystemError):
    pass

class PermissionDeniedError(FilesystemError):
    pass

class AtomicWriteError(FilesystemError):
    pass

class RollbackError(FilesystemError):
    pass

class BackupError(FilesystemError):
    pass

class InvalidPathError(FilesystemError):
    pass

class DirectoryNotEmptyError(FilesystemError):
    pass
