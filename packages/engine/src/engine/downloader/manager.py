from core.registry.base import RegistryProviderProtocol
from core.filesystem.base import FileSystemProtocol
from core.logging.logger import LoggerProtocol

from .models import DownloadRequest, DownloadResult
from .queue import QueueManager
from .worker import DownloadWorker
from .scheduler import DownloadScheduler
from .transfer import TransferEngine
from .verification import VerificationEngine
from .staging import StagingArea
from .progress import ProgressReporter
from .metrics import MetricsCollector

class DownloadManager:
    def __init__(self, provider: RegistryProviderProtocol, fs: FileSystemProtocol, logger: LoggerProtocol):
        self.fs = fs
        self.logger = logger
        self.provider = provider
        
        self.metrics = MetricsCollector()
        self.progress = ProgressReporter(logger)
        self.staging = StagingArea(fs)
        self.verification = VerificationEngine(fs)
        self.transfer = TransferEngine(provider, fs)
        
        self.worker = DownloadWorker(
            transfer=self.transfer,
            verification=self.verification,
            staging=self.staging,
            progress=self.progress,
            metrics=self.metrics
        )
        self.queue = QueueManager()
        self.scheduler = DownloadScheduler(self.queue, self.worker)
