from pathlib import Path
import tempfile
from core.filesystem.base import FileSystemProtocol

class StagingArea:
    def __init__(self, fs: FileSystemProtocol):
        self.fs = fs
        self.base_dir = Path(tempfile.gettempdir()) / "lifeofpy_staging"
        self.fs.create_directory(self.base_dir, parents=True)

    def prepare_stage(self, component_slug: str) -> Path:
        stage_dir = self.base_dir / component_slug
        if self.fs.exists(stage_dir):
            self.fs.delete_directory(stage_dir, recursive=True)
        self.fs.create_directory(stage_dir, parents=True)
        return stage_dir

    def cleanup_stage(self, component_slug: str):
        stage_dir = self.base_dir / component_slug
        if self.fs.exists(stage_dir):
            self.fs.delete_directory(stage_dir, recursive=True)
            
    def get_staged_path(self, component_slug: str) -> Path:
        return self.base_dir / component_slug
