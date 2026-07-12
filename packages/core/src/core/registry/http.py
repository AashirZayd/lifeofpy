import urllib.request
import urllib.error
import urllib.parse
from typing import Dict, Optional
import json
from .exceptions import NetworkError, RegistryTimeoutError, RegistryUnavailableError
from ..logging.logger import LoggerProtocol


class HttpClient:
    def __init__(self, logger: LoggerProtocol, timeout: int = 10, retries: int = 3):
        self.logger = logger
        self.timeout = timeout
        self.retries = retries

    def request_json(self, url: str, headers: Optional[Dict[str, str]] = None) -> dict:
        content = self.request_bytes(url, headers)
        try:
            return json.loads(content.decode("utf-8"))
        except json.JSONDecodeError as e:
            raise NetworkError(f"Failed to decode JSON from {url}: {e}") from e

    def request_bytes(self, url: str, headers: Optional[Dict[str, str]] = None) -> bytes:
        req_headers = headers or {}
        req_headers.setdefault("User-Agent", "LifeOfPy-CLI/1.0")

        req = urllib.request.Request(url, headers=req_headers)

        last_exception = None
        for attempt in range(self.retries):
            try:
                self.logger.debug(f"HTTP GET {url} (Attempt {attempt + 1}/{self.retries})")
                with urllib.request.urlopen(req, timeout=self.timeout) as response:
                    return response.read()
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    raise RegistryUnavailableError(f"Resource not found: {url}") from e
                last_exception = e
                self.logger.warning(f"HTTP {e.code} for {url}. Retrying...")
            except urllib.error.URLError as e:
                if isinstance(e.reason, TimeoutError):
                    last_exception = RegistryTimeoutError(f"Timeout fetching {url}")
                else:
                    last_exception = e
                self.logger.warning(f"Network error fetching {url}: {e}. Retrying...")
            except Exception as e:
                last_exception = e
                self.logger.warning(f"Unexpected error fetching {url}: {e}. Retrying...")

        raise NetworkError(
            f"Failed to fetch {url} after {self.retries} attempts. Last error: {last_exception}"
        )
