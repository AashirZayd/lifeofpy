from core.exceptions.base import LifeOfPyError

class InstallerError(LifeOfPyError):
    pass

class InstallError(InstallerError):
    pass

class WorkspaceError(InstallerError):
    pass

class CommitError(InstallerError):
    pass

class RollbackError(InstallerError):
    pass

class VerificationError(InstallerError):
    pass

class ProjectLockedError(InstallerError):
    pass

class HistoryError(InstallerError):
    pass

class TransactionError(InstallerError):
    pass
