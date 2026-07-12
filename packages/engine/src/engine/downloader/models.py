from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from .types import DownloadId
import time

class DownloadRequest(BaseModel):
    id: DownloadId
    component_slug: str
    version: str
    expected_checksum: Optional[str] = None
    priority: int = 0

class DownloadResult(BaseModel):
    id: DownloadId
    component_slug: str
    staged_path: str
    bytes_downloaded: int
    success: bool
    error_message: Optional[str] = None
    checksum: Optional[str] = None

class ProgressEvent(BaseModel):
    id: DownloadId
    status: str
    bytes_downloaded: int = 0
    total_bytes: int = 0
    message: Optional[str] = None

class DownloadMetrics(BaseModel):
    total_downloads: int = 0
    failed_downloads: int = 0
    retries: int = 0
    bytes_transferred: int = 0
    start_time: float = Field(default_factory=time.time)
    end_time: Optional[float] = None
    cache_hits: int = 0
    
    @property
    def average_download_time(self) -> float:
        if self.total_downloads == 0 or not self.end_time:
            return 0.0
        return (self.end_time - self.start_time) / self.total_downloads
