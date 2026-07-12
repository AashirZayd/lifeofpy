from typing import List
from .types import EventCallback
from .models import InstallEvent
from core.logging.logger import LoggerProtocol

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
