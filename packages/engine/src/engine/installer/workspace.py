from pathlib import Path
from core.filesystem.base import FileSystemProtocol
from .errors import WorkspaceError

class WorkspaceManager:
    def __init__(self, fs: FileSystemProtocol):
        self.fs = fs

    def create_workspace(self, project_dir: Path) -> Path:
        workspace_dir = project_dir / ".lifeofpy" / "workspace"
        try:
            if not self.fs.exists(workspace_dir):
                self.fs.create_directory(workspace_dir, parents=True)
            return workspace_dir
        except Exception as e:
            raise WorkspaceError(f"Failed to create workspace: {e}")

    def cleanup_workspace(self, workspace_dir: Path):
        try:
            if self.fs.exists(workspace_dir):
                self.fs.delete_directory(workspace_dir, recursive=True)
        except Exception as e:
            raise WorkspaceError(f"Failed to cleanup workspace: {e}")
