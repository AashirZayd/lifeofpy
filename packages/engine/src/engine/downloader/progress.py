from typing import Callable, List

from core.logging.logger import LoggerProtocol

from .models import ProgressEvent


class ProgressReporter:
    def __init__(self, logger: LoggerProtocol):
        self.logger = logger
        self.listeners: List[Callable[[ProgressEvent], None]] = []

    def subscribe(self, callback: Callable[[ProgressEvent], None]):
        self.listeners.append(callback)

    def report(self, event: ProgressEvent):
        self.logger.debug(f"Progress [{event.id}]: {event.status} ({event.bytes_downloaded}/{event.total_bytes})")
        for listener in self.listeners:
            listener(event)
