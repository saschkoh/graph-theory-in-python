"""
This module contains the core functionality for the graph_explorations package
"""
from oellrich_graph_in_python import Node, Edge, Graph

import heapq


class Dijkstra:
    """
    This class implements naive and modified Dijkstra's algorithms to find shortest paths in a
    graph.
    """
    def __init__(self, graph: Graph = None):
        self.graph = graph

    def min_distances(self, target_idx: int = None):
        """
        This method finds the shortest path betwen a target node and all other nodes in the graph
        using the backward difference.
        """
        # initialize the distances vector
        distances = [float("inf") for _ in range(self.graph.node_count)]
        distances[target_idx] = 0
        # initialize the backward neighbors heap
        heap = [(distances[target_idx], target_idx)]
        while heap:
            _, node_idx = heapq.heappop(heap)
            for edge in self.graph.nodes[node_idx].b_edges:
                if distances[edge.head.index] > distances[node_idx] + edge.weight:
                    distances[edge.head.index] = distances[node_idx] + edge.weight
                    heapq.heappush(heap, (distances[edge.weight], edge.head.index))
        return distances

    def shortest_path(self, source_idx: int = None, target_idx: int = None):
        """
        This method finds a shortest path between source and and target node using Dijkstra's
        algorithm.
        """
        distances = self.min_distances(source_idx)
        return distances[target_idx]


if __name__ == "__main__":
    node_a = Node("A", 0, 0, 0)
    node_b = Node("B", 1, 0, 1)
    node_c = Node("C", 1, 1, 2)
    edge_ab = Edge("AB", node_a, node_b, 0, 1)
    edge_bc = Edge("BC", node_b, node_c, 1, 2)

    test_graph = Graph(
        "test_graph",
        True,
        [node_a, node_b, node_c],
        [edge_ab, edge_bc]
    )
    dijkstra = Dijkstra(test_graph)
    back_diffs = dijkstra.min_distances(2)
    s_t_dist = dijkstra.shortest_path(0, 2)
    print(f"backward difference distances = {back_diffs}")
    print(f"s-t shortest distance = {s_t_dist}")
