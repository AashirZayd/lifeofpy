from pathlib import Path
import hashlib
from typing import Dict
from core.filesystem.base import FileSystemProtocol
from core.logging.logger import LoggerProtocol

class ChecksumGenerator:
    def __init__(self, logger: LoggerProtocol, fs: FileSystemProtocol):
        self.logger = logger
        self.fs = fs

    def generate_for_directory(self, directory: Path) -> Dict[str, str]:
        checksums = {}
        if not self.fs.exists(directory):
            return checksums
            
        files = sorted([f for f in Path(directory).rglob("*") if f.is_file()])
        
        for f in files:
            if f.name == "checksums.json":
                continue
                
            try:
                content = self.fs.read_bytes(f)
                sha = hashlib.sha256(content).hexdigest()
                rel_path = f.relative_to(directory).as_posix()
                checksums[rel_path] = sha
            except Exception as e:
                self.logger.warning(f"Failed to checksum {f}: {e}")
                
        return checksums
