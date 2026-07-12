import json
from pathlib import Path

from core.filesystem.base import FileSystemProtocol

from .errors import HistoryError
from .models import ComponentHistoryEntry, InstallHistory


class HistoryManager:
    def __init__(self, fs: FileSystemProtocol):
        self.fs = fs

    def record_install(self, project_dir: Path, slug: str, version: str):
        history_file = project_dir / ".lifeofpy" / "history.json"

        history = InstallHistory()
        if self.fs.exists(history_file):
            try:
                data = json.loads(self.fs.read_text(history_file))
                history = InstallHistory.model_validate(data)
            except Exception:
                pass

        history.entries.append(ComponentHistoryEntry(slug=slug, version=version, operation="install"))

        try:
            self.fs.create_directory(history_file.parent, parents=True)
            self.fs.write_text_atomic(history_file, json.dumps(history.model_dump(mode="json"), indent=2))
        except Exception as e:
            raise HistoryError(f"Failed to write history: {e}") from e
