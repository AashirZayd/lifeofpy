from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime


class Checksum(BaseModel):
    sha256: str


class RegistryMetadata(BaseModel):
    registryVersion: str
    schemaVersion: str
    engineVersion: str
    generatedAt: datetime
    componentCount: int
    frameworkCount: int
    categoryCount: int
    checksum: Checksum


class Framework(BaseModel):
    id: str
    name: str


class Category(BaseModel):
    id: str
    name: str


class Tag(BaseModel):
    id: str
    name: str


class ComponentManifest(BaseModel):
    schemaVersion: str = Field(default="1.0.0")
    id: str
    name: str
    description: str
    version: str
    author: str
    license: str
    supported_frameworks: List[str]
    pythonDependencies: List[str] = Field(default_factory=list)
    componentDependencies: List[str] = Field(default_factory=list)
    category: str
    tags: List[str] = Field(default_factory=list)
    preview: Optional[str] = None
    demo: Optional[str] = None
    checksums: Optional[Dict[str, str]] = None


class PackManifest(BaseModel):
    id: str
    name: str
    description: str
    components: List[str]
    author: str
    version: str


class SearchIndexEntry(BaseModel):
    id: str
    name: str
    description: str
    author: str
    tags: List[str]
    category: str
    frameworks: List[str]


class SearchIndex(BaseModel):
    entries: List[SearchIndexEntry]


class Registry(BaseModel):
    version: str
    metadata: RegistryMetadata
    components: List[ComponentManifest]
