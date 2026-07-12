from typing import Dict, List, Optional
from .models import DependencyNode, DependencyEdge
from .types import NodeId

class DependencyGraph:
    def __init__(self):
        self.nodes: Dict[NodeId, DependencyNode] = {}
        self.edges: List[DependencyEdge] = []
        self.adjacency_list: Dict[NodeId, List[NodeId]] = {}

    def add_node(self, node: DependencyNode):
        if node.id not in self.nodes:
            self.nodes[node.id] = node
            self.adjacency_list[node.id] = []

    def add_edge(self, source: NodeId, target: NodeId, constraint: Optional[str] = None):
        if source in self.nodes and target in self.nodes:
            self.edges.append(DependencyEdge(source=source, target=target, constraint=constraint))
            if target not in self.adjacency_list[source]:
                self.adjacency_list[source].append(target)

    def get_node(self, node_id: NodeId) -> Optional[DependencyNode]:
        return self.nodes.get(node_id)
        
    def get_dependencies(self, node_id: NodeId) -> List[NodeId]:
        return self.adjacency_list.get(node_id, [])
