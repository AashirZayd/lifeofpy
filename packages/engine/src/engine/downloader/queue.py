from typing import List, Optional

from .models import DownloadRequest


class QueueManager:
    def __init__(self):
        self.queue: List[DownloadRequest] = []

    def enqueue(self, request: DownloadRequest):
        self.queue.append(request)
        self.queue.sort(key=lambda req: req.priority, reverse=True)

    def dequeue(self) -> Optional[DownloadRequest]:
        if self.queue:
            return self.queue.pop(0)
        return None

    def cancel(self, request_id: str):
        self.queue = [req for req in self.queue if req.id != request_id]

    @property
    def is_empty(self) -> bool:
        return len(self.queue) == 0
