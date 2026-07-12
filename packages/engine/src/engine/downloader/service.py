from typing import List, Callable
from core.registry.base import RegistryProviderProtocol
from core.filesystem.base import FileSystemProtocol
from core.logging.logger import LoggerProtocol

from .models import DownloadRequest, DownloadResult, ProgressEvent
from .manager import DownloadManager
import uuid

class DownloaderService:
    def __init__(self, provider: RegistryProviderProtocol, fs: FileSystemProtocol, logger: LoggerProtocol):
        self.manager = DownloadManager(provider, fs, logger)

    def subscribe_progress(self, callback: Callable[[ProgressEvent], None]):
        self.manager.progress.subscribe(callback)

    def download(self, component_slug: str, version: str, expected_checksum: str = None) -> DownloadResult:
        req = DownloadRequest(
            id=str(uuid.uuid4()),
            component_slug=component_slug,
            version=version,
            expected_checksum=expected_checksum
        )
        self.manager.queue.enqueue(req)
        results = self.manager.scheduler.schedule()
        self.manager.metrics.finish()
        if results:
            return results[0]
        return DownloadResult(id=req.id, component_slug=component_slug, staged_path="", bytes_downloaded=0, success=False, error_message="Cancelled")

    def download_batch(self, components: List[dict]) -> List[DownloadResult]:
        for comp in components:
            req = DownloadRequest(
                id=str(uuid.uuid4()),
                component_slug=comp["slug"],
                version=comp.get("version", "latest"),
                expected_checksum=comp.get("checksum")
            )
            self.manager.queue.enqueue(req)
            
        results = self.manager.scheduler.schedule()
        self.manager.metrics.finish()
        return results

    def cancel(self):
        self.manager.scheduler.cancel_all()

    def status(self) -> dict:
        return self.manager.metrics.get_metrics()

    def verify(self, result: DownloadResult) -> bool:
        return result.success

    def cleanup(self, component_slug: str):
        self.manager.staging.cleanup_stage(component_slug)
