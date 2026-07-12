from typing import List, Dict, Set
from .graph import DependencyGraph
from .models import Cycle
from .types import NodeId
from engine.validator.diagnostics import Diagnostic, Severity

class CycleDetector:
    def detect(self, graph: DependencyGraph) -> List[Diagnostic]:
        visited: Set[NodeId] = set()
        rec_stack: Set[NodeId] = set()
        path: List[NodeId] = []
        diagnostics: List[Diagnostic] = []

        def dfs(node: NodeId):
            visited.add(node)
            rec_stack.add(node)
            path.append(node)

            for neighbor in sorted(graph.get_dependencies(node)):
                if neighbor not in visited:
                    dfs(neighbor)
                elif neighbor in rec_stack:
                    cycle_start_index = path.index(neighbor)
                    cycle_path = path[cycle_start_index:] + [neighbor]
                    
                    diagnostics.append(Diagnostic(
                        severity=Severity.ERROR,
                        code="DEP-CYC-001",
                        title="Circular Dependency Detected",
                        description=f"Cycle: {' -> '.join(cycle_path)}",
                        suggestion="Refactor components to break the circular dependency."
                    ))

            rec_stack.remove(node)
            path.pop()

        for node in sorted(graph.nodes.keys()):
            if node not in visited:
                dfs(node)

        return diagnostics
