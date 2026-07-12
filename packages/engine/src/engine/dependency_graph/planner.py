from typing import List
from .models import InstallPlan, InstallPlanStage, ResolutionResult
from .sorter import TopologicalSorter
from .errors import PlanningError

class InstallationPlanner:
    def __init__(self, sorter: TopologicalSorter):
        self.sorter = sorter

    def plan(self, resolution: ResolutionResult) -> InstallPlan:
        if resolution.has_errors:
            raise PlanningError("Cannot generate install plan from a resolution with errors.")

        from .graph import DependencyGraph
        graph = DependencyGraph()
        for node in resolution.resolved_nodes:
            graph.add_node(node)
        for edge in resolution.edges:
            graph.add_edge(edge.source, edge.target)

        try:
            sorted_nodes = self.sorter.sort(graph)
        except Exception as e:
            raise PlanningError(f"Failed to sort dependencies: {e}")

        stages = [
            InstallPlanStage(name="Resolve", components=[]),
            InstallPlanStage(name="Download", components=sorted_nodes.copy()),
            InstallPlanStage(name="Install", components=sorted_nodes.copy()),
            InstallPlanStage(name="Verify", components=sorted_nodes.copy()),
        ]

        return InstallPlan(
            stages=stages,
            total_components=len(sorted_nodes),
            diagnostics=resolution.diagnostics
        )
