from core.exceptions.base import LifeOfPyError

class DownloaderError(LifeOfPyError):
    pass

class DownloadError(DownloaderError):
    pass

class TransferError(DownloaderError):
    pass

class VerificationError(DownloaderError):
    pass

class ChecksumMismatchError(VerificationError):
    pass

class NetworkFailureError(DownloaderError):
    pass

class ResumeError(DownloaderError):
    pass

class QueueError(DownloaderError):
    pass

class CancellationError(DownloaderError):
    pass

class TimeoutError(DownloaderError):
    pass
