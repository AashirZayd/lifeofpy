from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Set
from .types import NodeId, VersionString, FrameworkName
from engine.validator.diagnostics import Diagnostic

class DependencyNode(BaseModel):
    id: NodeId
    version: VersionString
    frameworks: List[FrameworkName]
    dependencies: List[NodeId]
    metadata: Dict[str, str] = Field(default_factory=dict)
    checksum: Optional[str] = None
    installation_status: str = "pending"

class DependencyEdge(BaseModel):
    source: NodeId
    target: NodeId
    constraint: Optional[str] = None

class Conflict(BaseModel):
    code: str
    description: str
    affected_components: List[NodeId]
    suggestion: Optional[str] = None

class Cycle(BaseModel):
    path: List[NodeId]
    description: str

class ResolutionResult(BaseModel):
    resolved_nodes: List[DependencyNode]
    edges: List[DependencyEdge]
    diagnostics: List[Diagnostic] = Field(default_factory=list)
    has_errors: bool = False

class InstallPlanStage(BaseModel):
    name: str
    components: List[NodeId]

class InstallPlan(BaseModel):
    stages: List[InstallPlanStage]
    total_components: int
    diagnostics: List[Diagnostic] = Field(default_factory=list)

class Constraint(BaseModel):
    raw: str
    parsed: str

class LockEntry(BaseModel):
    id: NodeId
    version: VersionString
    checksum: str
    dependencies: List[NodeId]
