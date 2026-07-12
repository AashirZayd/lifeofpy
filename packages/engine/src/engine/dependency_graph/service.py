from typing import List, Dict
from core.logging.logger import LoggerProtocol
from .models import DependencyNode, ResolutionResult, InstallPlan
from .resolver import DependencyResolver
from .planner import InstallationPlanner
from .cycles import CycleDetector
from .conflicts import ConflictDetector
from .sorter import TopologicalSorter
from .graph import DependencyGraph

class DependencyGraphService:
    def __init__(self, logger: LoggerProtocol):
        self.logger = logger
        self.cycle_detector = CycleDetector()
        self.conflict_detector = ConflictDetector()
        self.resolver = DependencyResolver(self.cycle_detector, self.conflict_detector)
        self.sorter = TopologicalSorter()
        self.planner = InstallationPlanner(self.sorter)

    def resolve(self, requested_nodes: List[DependencyNode], available_nodes: Dict[str, DependencyNode], target_framework: str = None) -> ResolutionResult:
        self.logger.info("Resolving dependencies")
        return self.resolver.resolve(requested_nodes, available_nodes, target_framework)

    def plan(self, resolution: ResolutionResult) -> InstallPlan:
        self.logger.info("Generating installation plan")
        return self.planner.plan(resolution)

    def validate(self, graph: DependencyGraph) -> List:
        cycles = self.cycle_detector.detect(graph)
        conflicts = self.conflict_detector.detect(graph)
        return cycles + conflicts

    def sort(self, graph: DependencyGraph) -> List[str]:
        return self.sorter.sort(graph)

    def detect_cycles(self, graph: DependencyGraph) -> List:
        return self.cycle_detector.detect(graph)

    def detect_conflicts(self, graph: DependencyGraph, target_framework: str = None) -> List:
        return self.conflict_detector.detect(graph, target_framework)

    def verify(self, plan: InstallPlan) -> bool:
        return not any(d.severity.value == "ERROR" for d in plan.diagnostics)
