import json
from pathlib import Path

from core.filesystem.base import FileSystemProtocol

from .models import LockfileEntry, ProjectLockfile


class LockfileManager:
    def __init__(self, fs: FileSystemProtocol):
        self.fs = fs

    def update_lockfile(self, project_dir: Path, slug: str, version: str, dependencies: list, checksum: str):
        lock_file = project_dir / "lifeofpy.lock"

        lockfile = ProjectLockfile()
        if self.fs.exists(lock_file):
            try:
                data = json.loads(self.fs.read_text(lock_file))
                lockfile = ProjectLockfile.model_validate(data)
            except Exception:
                pass

        lockfile.components[slug] = LockfileEntry(
            slug=slug, version=version, checksum=checksum, dependencies=dependencies
        )

        self.fs.write_text_atomic(lock_file, json.dumps(lockfile.model_dump(), indent=2))
