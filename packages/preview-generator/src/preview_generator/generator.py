from abc import ABC, abstractmethod
from pathlib import Path

class PreviewGenerator(ABC):
    """
    Architecture for running a demo.py script and capturing a WebP preview.
    Future implementation will use subprocess and headless screenshot tools.
    """
    
    @abstractmethod
    def generate(self, demo_path: Path, output_dir: Path) -> Path:
        """Executes demo.py and captures the UI into a responsive WebP thumbnail."""
        pass
