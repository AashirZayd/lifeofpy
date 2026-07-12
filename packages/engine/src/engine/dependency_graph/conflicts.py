from typing import List

from engine.validator.diagnostics import Diagnostic, Severity

from .graph import DependencyGraph


class ConflictDetector:
    def detect(self, graph: DependencyGraph, target_framework: str = None) -> List[Diagnostic]:
        diagnostics = []

        for node_id, node in graph.nodes.items():
            if target_framework and target_framework not in node.frameworks:
                diagnostics.append(
                    Diagnostic(
                        severity=Severity.ERROR,
                        code="DEP-CNF-001",
                        title="Framework Mismatch",
                        description=f"Component '{node_id}' does not support framework '{target_framework}'.",
                        suggestion="Ensure all dependencies support the target framework.",
                    )
                )

        return diagnostics
