from typing import List, Set

from .errors import CycleDetectedError
from .graph import DependencyGraph
from .types import NodeId


class TopologicalSorter:
    def sort(self, graph: DependencyGraph) -> List[NodeId]:
        visited: Set[NodeId] = set()
        temp_mark: Set[NodeId] = set()
        result: List[NodeId] = []

        def visit(node: NodeId):
            if node in temp_mark:
                raise CycleDetectedError(f"Cannot sort graph with cycles at {node}")
            if node not in visited:
                temp_mark.add(node)

                for neighbor in sorted(graph.get_dependencies(node)):
                    visit(neighbor)

                temp_mark.remove(node)
                visited.add(node)
                result.append(node)

        for node in sorted(graph.nodes.keys()):
            if node not in visited:
                visit(node)

        return result
