from core.filesystem.base import FileSystemProtocol
from core.logging.logger import LoggerProtocol
from core.registry.base import RegistryProviderProtocol

from .metrics import MetricsCollector
from .progress import ProgressReporter
from .queue import QueueManager
from .scheduler import DownloadScheduler
from .staging import StagingArea
from .transfer import TransferEngine
from .verification import VerificationEngine
from .worker import DownloadWorker


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
            metrics=self.metrics,
        )
        self.queue = QueueManager()
        self.scheduler = DownloadScheduler(self.queue, self.worker)
