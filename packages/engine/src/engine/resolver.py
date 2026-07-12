from typing import Dict, List, Set


class CircularDependencyError(Exception):
    pass


class DependencyResolver:
    def __init__(self):
        # map of component_id -> list of dependent component_ids
        self.graph: Dict[str, List[str]] = {}

    def add_node(self, component_id: str, dependencies: List[str]):
        self.graph[component_id] = dependencies

    def resolve(self, component_id: str) -> List[str]:
        """Returns a flat list of all dependencies in topological order."""
        visited: Set[str] = set()
        path: Set[str] = set()
        result: List[str] = []

        def dfs(node: str):
            if node in path:
                raise CircularDependencyError(f"Circular dependency detected: {' -> '.join(path)} -> {node}")
            if node in visited:
                return

            path.add(node)
            for dep in self.graph.get(node, []):
                dfs(dep)
            path.remove(node)
            visited.add(node)
            result.append(node)

        dfs(component_id)
        if component_id in result:
            result.remove(component_id)
        return result
