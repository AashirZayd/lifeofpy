from typing import List

from .errors import CancellationError
from .models import DownloadResult
from .queue import QueueManager
from .worker import DownloadWorker


class DownloadScheduler:
    def __init__(self, queue: QueueManager, worker: DownloadWorker):
        self.queue = queue
        self.worker = worker
        self.cancelled = False

    def schedule(self) -> List[DownloadResult]:
        results = []
        while not self.queue.is_empty:
            if self.cancelled:
                raise CancellationError("Download scheduler was cancelled.")

            request = self.queue.dequeue()
            if request:
                result = self.worker.execute(request)
                results.append(result)

        return results

    def cancel_all(self):
        self.cancelled = True
