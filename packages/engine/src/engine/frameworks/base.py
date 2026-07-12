from abc import ABC, abstractmethod


class FrameworkAdapter(ABC):
    @property
    @abstractmethod
    def id(self) -> str:
        """The framework ID, e.g., 'customtkinter'"""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Human readable name"""
        pass

    @abstractmethod
    def validate_component(self, component_path: str) -> bool:
        """Framework specific validation logic for a component."""
        pass
