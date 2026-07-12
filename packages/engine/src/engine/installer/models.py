from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime, timezone
import time

class InstallEvent(BaseModel):
    name: str
    component_slug: Optional[str] = None
    message: Optional[str] = None
    timestamp: float = Field(default_factory=time.time)

class ComponentHistoryEntry(BaseModel):
    slug: str
    version: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    operation: str
    registry_version: str = "1.0.0"
    engine_version: str = "0.1.0"

class InstallHistory(BaseModel):
    entries: List[ComponentHistoryEntry] = Field(default_factory=list)

class LockfileEntry(BaseModel):
    slug: str
    version: str
    checksum: str
    dependencies: List[str] = Field(default_factory=list)

class ProjectLockfile(BaseModel):
    version: str = "1.0.0"
    registry_version: str = "1.0.0"
    framework: str = "unknown"
    components: Dict[str, LockfileEntry] = Field(default_factory=dict)
