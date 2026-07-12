# LifeOfPy Dependency Graph Engine

The Dependency Graph Engine is the canonical resolver for every component installation within LifeOfPy. 

## Architecture
The engine builds a directed graph of all required components, enforcing deterministic topological sorting, deep cycle detection, and framework conflict resolution before the installer touches any files.

1. **Resolution (`resolver.py`)**: Traverses `DependencyNode` representations to build the graph and confirm availability.
2. **Cycle Detection (`cycles.py`)**: Enforces strict acyclic constraints using DFS trace-paths. Returns compiler-style diagnostics pointing exactly to the cycle.
3. **Conflict Detection (`conflicts.py`)**: Blocks installations attempting to merge incompatible frameworks.
4. **Planning (`planner.py`)**: Consumes the `ResolutionResult` to generate an `InstallPlan`, sorting dependencies bottom-up (leaves first) so the Installer resolves dependencies in a safe order.

## Public API

```python
from engine.dependency_graph.service import DependencyGraphService
from core.logging.logger import DefaultLogger

logger = DefaultLogger()
engine = DependencyGraphService(logger)

# Generates a ResolutionResult highlighting errors, missing packages, or cycles
resolution = engine.resolve(requested_nodes, available_nodes_map, target_framework="customtkinter")

if not resolution.has_errors:
    # Generates a strictly-sorted execution plan
    plan = engine.plan(resolution)
    # The installer can blindly execute this plan in sequence.
```
