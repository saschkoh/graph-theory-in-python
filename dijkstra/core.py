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

    def dijkstra_dist(self, i_target: int = None) -> list[float]:
        """
        This method finds the shortest paths betwen a target node and all other nodes in the graph
        using the backward difference.
        """
        # initialize the distances vector with infinity
        distances = [float("inf") for _ in range(self.graph.node_count)]
        # set the distance of the target node to zero
        distances[i_target] = 0
        # initialize the heap with the target node's zero distance and index
        heap = [(distances[i_target], i_target)]
        while heap:
            # get the node with the smallest distance
            _, i_node = heapq.heappop(heap)
            # iterate over all backward edges of the node
            for edge in self.graph.nodes[i_node].b_edges:
                if distances[edge.head.index] > distances[i_node] + edge.weight:
                    distances[edge.head.index] = distances[i_node] + edge.weight
                    heapq.heappush(heap, (distances[edge.head.index], edge.head.index))
        return distances

    def dijkstra(
            self,
            i_source: int = None,
            i_target: int = None,
            dist: list = None,
            count: bool = False
            ) -> tuple[float, list[int], int]:
        """
        This method finds a shortest path between source and and target node using Dijkstra's
        algorithm.
        """
        # initialize the distances vector with infinity and the predecessor vector with None
        distances = [float("inf") for _ in range(self.graph.node_count)]
        predecessors = [None for _ in range(self.graph.node_count)]
        # initilize the distance of the source node with 0 or backward difference if given
        distances[i_source] = 0 if dist is None else dist[i_source]
        # mark the source node as its own predecessor
        predecessors[i_source] = i_source
        # initialize the heap with the source node and its distance
        heap = [(distances[i_source], i_source)]
        counter = 0 if count else None
        while heap:
            # get the node with the smallest distance
            _, i_node = heapq.heappop(heap)
            # stop if the target node is reached
            if i_node == i_target:
                break
            counter += 1 if count else None
            # iterate over all forward edges of the node
            for edge in self.graph.nodes[i_node].f_edges:
                if dist is not None:
                    # calculate modified edge weight in case of backward difference is used
                    weight = edge.weight - dist[i_node] + dist[edge.tail.index]
                else:
                    # use unmodified edge weight instead
                    weight = edge.weight
                # update the distance and predecessor if a shorter distance is found
                if distances[edge.tail.index] > distances[i_node] + weight:
                    distances[edge.tail.index] = distances[i_node] + weight
                    predecessors[edge.tail.index] = i_node
                    # add the shorter distance and node index to the heap
                    heapq.heappush(heap, (distances[edge.tail.index], edge.tail.index))
        return distances[i_target], predecessors, counter if count else distances[i_target], predecessors


if __name__ == "__main__":
    tests = {
        "test10": GraphReader("./graphs/test10.gra", True).read(),
        "deutschland1": GraphReader("./graphs/deutschland1.gra", True).read()
    }

    test_graph = tests["test10"]
    # test_graph = tests["deutschland1"]

    stuttgart_idx = test_graph.node_by_name("711000").index
    berlin_idx = test_graph.node_by_name("300000").index

    dijkstra = Dijkstra(test_graph)
    back_diffs = dijkstra.dijkstra_dist(stuttgart_idx)
    print(f"backward difference distances = {back_diffs}")
    s_t_dist, pre_nodes, iter = dijkstra.dijkstra(berlin_idx, stuttgart_idx)
    print(f"i:{iter} s-t shortest distance = {s_t_dist}")
    s_t_dist, pre_nodes, iter = dijkstra.dijkstra(berlin_idx, stuttgart_idx, back_diffs)
    print(f"i: {iter} s-t shortest distance with dist = {s_t_dist}")
    print(f"predecessors with dist = {pre_nodes}")
