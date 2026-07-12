from typing import List

from core.logging.logger import LoggerProtocol

from .models import InstallEvent
from .types import EventCallback


class EventBus:
    def __init__(self, logger: LoggerProtocol):
        self.logger = logger
        self.listeners: List[EventCallback] = []

    def subscribe(self, callback: EventCallback):
        self.listeners.append(callback)

    def emit(self, event: InstallEvent):
        self.logger.debug(f"Installer Event: {event.name} - {event.component_slug} - {event.message}")
        for listener in self.listeners:
            listener(event)
