from typing import Optional, Any
from pathlib import Path
import json
import time
from ..filesystem.base import FileSystemProtocol
from ..logging.logger import LoggerProtocol


class RegistryCache:
    def __init__(
        self, fs: FileSystemProtocol, logger: LoggerProtocol, cache_dir: Path, ttl: int = 3600
    ):
        self.fs = fs
        self.logger = logger
        self.cache_dir = cache_dir
        self.ttl = ttl

        if not self.fs.exists(self.cache_dir):
            self.fs.create_directory(self.cache_dir, parents=True)

    def get(self, key: str) -> Optional[Any]:
        safe_key = key.replace("/", "_").replace(":", "_")
        cache_path = self.cache_dir / f"{safe_key}.json"

        if not self.fs.exists(cache_path):
            self.logger.debug(f"Cache miss for {key}")
            return None

        try:
            content = self.fs.read_text(cache_path)
            data = json.loads(content)

            if time.time() - data.get("timestamp", 0) > self.ttl:
                self.logger.debug(f"Cache expired for {key}")
                return None

            self.logger.debug(f"Cache hit for {key}")
            return data.get("value")
        except Exception as e:
            self.logger.warning(f"Failed to read cache for {key}: {e}")
            return None

    def set(self, key: str, value: Any) -> None:
        safe_key = key.replace("/", "_").replace(":", "_")
        cache_path = self.cache_dir / f"{safe_key}.json"

        try:
            data = {"timestamp": time.time(), "value": value}
            self.fs.write_text_atomic(cache_path, json.dumps(data))
            self.logger.debug(f"Cached {key}")
        except Exception as e:
            self.logger.warning(f"Failed to write cache for {key}: {e}")
