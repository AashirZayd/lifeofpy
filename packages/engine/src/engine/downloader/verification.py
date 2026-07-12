import hashlib
from pathlib import Path

from core.filesystem.base import FileSystemProtocol

from .errors import ChecksumMismatchError, VerificationError


class VerificationEngine:
    def __init__(self, fs: FileSystemProtocol):
        self.fs = fs

    def verify_checksum(self, file_path: Path, expected_sha256: str) -> bool:
        if not self.fs.exists(file_path):
            raise VerificationError(f"File not found for verification: {file_path}")

        content = self.fs.read_bytes(file_path)
        actual_sha = hashlib.sha256(content).hexdigest()

        if actual_sha != expected_sha256:
            raise ChecksumMismatchError(
                f"Checksum mismatch for {file_path}. Expected {expected_sha256}, got {actual_sha}"
            )
        return True

    def verify_size(self, file_path: Path, min_size: int = 1) -> bool:
        if not self.fs.exists(file_path):
            raise VerificationError(f"File not found for verification: {file_path}")

        content = self.fs.read_bytes(file_path)
        if len(content) < min_size:
            raise VerificationError(f"File {file_path} is suspiciously small: {len(content)} bytes")
        return True
