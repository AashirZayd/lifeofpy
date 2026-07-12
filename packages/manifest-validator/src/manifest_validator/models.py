from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from datetime import datetime

class ComponentManifest(BaseModel):
    schemaVersion: str = Field(default="1.0.0")
    id: str = Field(..., description="Unique identifier (e.g., button-01)")
    name: str = Field(..., description="Human readable name")
    description: str = Field(..., description="Short description")
    version: str = Field(..., description="Semantic version (e.g., 1.0.0)")
    author: str = Field(...)
    license: str = Field(...)
    supported_frameworks: List[str] = Field(..., min_length=1)
    dependencies: List[str] = Field(default_factory=list)
    category: str = Field(...)
    tags: List[str] = Field(default_factory=list)
    keywords: List[str] = Field(default_factory=list)
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)
    repository: Optional[HttpUrl] = None
    homepage: Optional[HttpUrl] = None
    documentation: Optional[HttpUrl] = None
    preview: Optional[str] = Field(None, description="Path to preview image")
    demo: Optional[str] = Field(None, description="Path to demo script")
    checksum: Optional[str] = None

class PackManifest(BaseModel):
    schemaVersion: str = Field(default="1.0.0")
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    components: List[str] = Field(..., description="List of component IDs included in this pack")
    author: str = Field(...)
    version: str = Field(...)
