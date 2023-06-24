"""
This module contains the core functionality for the graph_explorations package
"""
from graph.core import Node, Edge, Graph

import heapq


class Dijkstra:
    """
    This class implements naive and modified Dijkstra's algorithms to find shortest paths in a graph.
    """
    def __init__(self, graph: Graph = None):
        self.graph = graph

    def back_diff(self, target_idx: int = None):
        """
        This method finds the shortest path betwen a target node and all other nodes in the graph using the backward
        difference.
        """
        # initialize the distances vector
        distances = [float("inf") for _ in range(len(self.graph.node_count))]
        distances[target_idx] = 0
        # initialize the predecessors heap
        heap = [(dict[target_idx], target_idx)]
        while heap:
            _, node_index = heapq.heappop(heap)
            for edge in self.graph.nodes[node_index].b_edges:
                if distances[edge.head.index] > distances[node_index] + edge.weight:
                    distances[edge.head.index] = distances[edge.node_index] + edge.weight
                    heapq.heappush(heap, (distances[edge.weight], edge.head.index))
        return distances

    def shortest_path(self, source_idx: int = None, target_idx: int = None):
        """
        This method finds a shortest path between source and and target_idx node using Dijkstra's algorithm
        """
        pass


if __name__ == "__main__":
    node_a = Node("A", 0, 0, 0)
    node_b = Node("B", 1, 0, 1)
    node_c = Node("C", 1, 1, 2)
    edge_ab = Edge("AB", node_a, node_b, 0, 1)
    edge_bc = Edge("BC", node_b, node_c, 1, 2)

    graph = Graph(
        "test_graph",
        True,
        [node_a, node_b, node_c],
        [edge_ab, edge_bc]
    )
    shortest_paths = Dijkstra(graph).back_diff(2)
    print(shortest_paths)
