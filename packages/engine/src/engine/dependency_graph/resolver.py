from typing import Dict, List, Set

from engine.validator.diagnostics import Diagnostic, Severity

from .conflicts import ConflictDetector
from .cycles import CycleDetector
from .graph import DependencyGraph
from .models import DependencyNode, ResolutionResult
from .types import NodeId


class DependencyResolver:
    def __init__(self, cycle_detector: CycleDetector, conflict_detector: ConflictDetector):
        self.cycle_detector = cycle_detector
        self.conflict_detector = conflict_detector

    def resolve(
        self,
        requested_nodes: List[DependencyNode],
        available_nodes: Dict[NodeId, DependencyNode],
        target_framework: str = None,
    ) -> ResolutionResult:
        graph = DependencyGraph()
        diagnostics: List[Diagnostic] = []

        queue = [node.id for node in requested_nodes]
        for node in requested_nodes:
            graph.add_node(node)

        visited: Set[NodeId] = {n.id for n in requested_nodes}

        while queue:
            current_id = queue.pop(0)
            current_node = graph.get_node(current_id)

            for dep_id in sorted(current_node.dependencies):
                if dep_id not in available_nodes:
                    diagnostics.append(
                        Diagnostic(
                            severity=Severity.ERROR,
                            code="DEP-RES-001",
                            title="Missing Dependency",
                            description=f"Component '{dep_id}' (required by '{current_id}') is not available.",
                            suggestion=f"Ensure '{dep_id}' exists in the registry.",
                        )
                    )
                    continue

                dep_node = available_nodes[dep_id]
                graph.add_node(dep_node)
                graph.add_edge(current_id, dep_id)

                if dep_id not in visited:
                    visited.add(dep_id)
                    queue.append(dep_id)

        cycle_diags = self.cycle_detector.detect(graph)
        diagnostics.extend(cycle_diags)

        conflict_diags = self.conflict_detector.detect(graph, target_framework)
        diagnostics.extend(conflict_diags)

        has_errors = any(d.severity == Severity.ERROR for d in diagnostics)

        return ResolutionResult(
            resolved_nodes=list(graph.nodes.values()), edges=graph.edges, diagnostics=diagnostics, has_errors=has_errors
        )
