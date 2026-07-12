from .models import DownloadMetrics


class MetricsCollector:
    def __init__(self):
        self.metrics = DownloadMetrics()

    def record_success(self, bytes_downloaded: int, cache_hit: bool = False):
        self.metrics.total_downloads += 1
        self.metrics.bytes_transferred += bytes_downloaded
        if cache_hit:
            self.metrics.cache_hits += 1

    def record_failure(self):
        self.metrics.total_downloads += 1
        self.metrics.failed_downloads += 1

    def record_retry(self):
        self.metrics.retries += 1

    def finish(self):
        import time

        self.metrics.end_time = time.time()

    def get_metrics(self) -> dict:
        return self.metrics.model_dump()
