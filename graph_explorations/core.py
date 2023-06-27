"""
This module contains the core functionality for the graph_explorations package
"""
from oellrich_graph import Node, Edge, Graph, GraphReader

import heapq


class Dijkstra:
    """
    This class implements naive and modified Dijkstra's algorithms to find shortest paths in a
    graph.
    """
    def __init__(self, graph: Graph = None):
        self.graph = graph

    def dijkstra_dist(self, target_idx: int = None):
        """
        This method finds the shortest paths betwen a target node and all other nodes in the graph
        using the backward difference.
        """
        # initialize the distances vector
        distances = [float("inf") for _ in range(self.graph.node_count)]
        distances[target_idx] = 0
        # initialize the heap with the target node and its distance
        heap = [(distances[target_idx], target_idx)]
        while heap:
            _, node_idx = heapq.heappop(heap)
            for edge in self.graph.nodes[node_idx].b_edges:
                if distances[edge.head.index] > distances[node_idx] + edge.weight:
                    distances[edge.head.index] = distances[node_idx] + edge.weight
                    heapq.heappush(heap, (distances[edge.head.index], edge.head.index))
        return distances

    def dijkstra(self, source_idx: int = None, target_idx: int = None, dist: list = None):
        """
        This method finds a shortest path between source and and target node using Dijkstra's
        algorithm.
        """
        distances = [float("inf") for _ in range(self.graph.node_count)]
        predecessors = [None for _ in range(self.graph.node_count)]
        distances[source_idx] = 0 if dist is None else dist[source_idx]
        predecessors[source_idx] = source_idx
        heap = [(distances[source_idx], source_idx)]
        iter = 0
        while heap:
            _, node_idx = heapq.heappop(heap)
            if node_idx == target_idx:
                break
            iter += 1
            for edge in self.graph.nodes[node_idx].f_edges:
                if dist is not None:
                    # modified edge weight
                    weight = edge.weight - dist[node_idx] + dist[edge.tail.index]
                else:
                    weight = edge.weight
                if distances[edge.tail.index] > distances[node_idx] + weight:
                    distances[edge.tail.index] = distances[node_idx] + weight
                    predecessors[edge.tail.index] = node_idx
                    heapq.heappush(heap, (distances[edge.tail.index], edge.tail.index))
        return distances[target_idx], predecessors, iter


if __name__ == "__main__":
    node_a = Node("A", 0, 0, 0)
    node_b = Node("B", 1, 0, 1)
    node_c = Node("C", 1, 1, 2)
    edge_ab = Edge("AB", node_a, node_b, 0, 1)
    edge_bc = Edge("BC", node_b, node_c, 1, 2)

    test_graph_1 = Graph(
        "test_graph",
        True,
        [node_a, node_b, node_c],
        [edge_ab, edge_bc]
    )
    test_graph_2 = GraphReader("./graphs/deutschland1.gra", True).read()
    stuttgart_idx = test_graph_2.node_by_name("711000").index
    berlin_idx = test_graph_2.node_by_name("300000").index
    print(f"stuttgart {stuttgart_idx} berlin {berlin_idx}")
    dijkstra = Dijkstra(test_graph_2)
    back_diffs = dijkstra.dijkstra_dist(stuttgart_idx)
    print(f"backward difference distances = {back_diffs}")
    s_t_dist, pre_nodes, iter = dijkstra.dijkstra(berlin_idx, stuttgart_idx)
    print(f"i:{iter} s-t shortest distance = {s_t_dist}")
    s_t_dist, pre_nodes, iter = dijkstra.dijkstra(berlin_idx, stuttgart_idx, back_diffs)
    print(f"i: {iter} s-t shortest distance with dist = {s_t_dist}")
    print(f"predecessors with dist = {pre_nodes}")
