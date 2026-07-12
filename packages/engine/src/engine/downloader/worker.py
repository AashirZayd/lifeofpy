from .errors import ChecksumMismatchError, NetworkFailureError
from .metrics import MetricsCollector
from .models import DownloadRequest, DownloadResult, ProgressEvent
from .progress import ProgressReporter
from .staging import StagingArea
from .transfer import TransferEngine
from .verification import VerificationEngine


class DownloadWorker:
    def __init__(
        self,
        transfer: TransferEngine,
        verification: VerificationEngine,
        staging: StagingArea,
        progress: ProgressReporter,
        metrics: MetricsCollector,
    ):
        self.transfer = transfer
        self.verification = verification
        self.staging = staging
        self.progress = progress
        self.metrics = metrics

    def execute(self, request: DownloadRequest) -> DownloadResult:
        self.progress.report(ProgressEvent(id=request.id, status="queued"))

        try:
            self.progress.report(ProgressEvent(id=request.id, status="downloading"))
            stage_dir = self.staging.prepare_stage(request.component_slug)

            bytes_downloaded = 0
            retries = 3
            for attempt in range(retries):
                try:
                    bytes_downloaded = self.transfer.download_component(
                        request.component_slug, request.version, stage_dir
                    )
                    break
                except NetworkFailureError as e:
                    self.metrics.record_retry()
                    if attempt == retries - 1:
                        raise e

            self.progress.report(
                ProgressEvent(
                    id=request.id, status="verifying", bytes_downloaded=bytes_downloaded, total_bytes=bytes_downloaded
                )
            )

            manifest_file = stage_dir / "manifest.json"
            if request.expected_checksum and manifest_file.exists():
                self.verification.verify_checksum(manifest_file, request.expected_checksum)

            self.metrics.record_success(bytes_downloaded)
            self.progress.report(
                ProgressEvent(
                    id=request.id, status="completed", bytes_downloaded=bytes_downloaded, total_bytes=bytes_downloaded
                )
            )

            return DownloadResult(
                id=request.id,
                component_slug=request.component_slug,
                staged_path=str(stage_dir),
                bytes_downloaded=bytes_downloaded,
                success=True,
            )

        except ChecksumMismatchError as e:
            self.metrics.record_failure()
            self.progress.report(ProgressEvent(id=request.id, status="failed", message=str(e)))
            self.staging.cleanup_stage(request.component_slug)
            return DownloadResult(
                id=request.id,
                component_slug=request.component_slug,
                staged_path="",
                bytes_downloaded=0,
                success=False,
                error_message=str(e),
            )

        except Exception as e:
            self.metrics.record_failure()
            self.progress.report(ProgressEvent(id=request.id, status="failed", message=str(e)))
            self.staging.cleanup_stage(request.component_slug)
            return DownloadResult(
                id=request.id,
                component_slug=request.component_slug,
                staged_path="",
                bytes_downloaded=0,
                success=False,
                error_message=str(e),
            )
