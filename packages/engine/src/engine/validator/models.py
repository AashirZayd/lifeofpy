from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class ValidatorManifest(BaseModel):
    schemaVersion: str = Field(default="1.0.0")
    manifestVersion: str = Field(default="1.0.0")
    id: str
    slug: str
    name: str
    description: str
    version: str
    author: str
    license: str
    repository: Optional[str] = None
    homepage: Optional[str] = None
    documentation: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    category: str
    tags: List[str] = Field(default_factory=list)
    keywords: List[str] = Field(default_factory=list)
    supportedFrameworks: List[str]
    componentDependencies: List[str] = Field(default_factory=list)
    pythonDependencies: List[str] = Field(default_factory=list)
    preview: Optional[str] = None
    demo: Optional[str] = None
    readme: Optional[str] = None
    checksum: Optional[str] = None
    experimental: bool = False
    deprecated: bool = False
