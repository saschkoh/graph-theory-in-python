# write a class that will be used to explore graphs
# the class will be instantiated with a graph
# the class will have methods to explore the graph
# the class will have methods to return the results of the exploration
# the class will have a method to find the shortest path between two nodes
# this method will have and argument which will define the algorithm to use
# one of the algorithms will be Dijkstra's algorithm


from graph import Graph
from dijkstra import core as dc


class GraphExploration():
    """
    A class to explore graphs for explorations such as finding the shortest path between two nodes
    """
    def __init__(self, graph: Graph = None):
        if graph is None:
            raise ValueError("No graph specified")
        if isinstance(graph, Graph) is False:
            raise TypeError(
                f"GraphExploration: Graph must be of type Graph, type {type(graph)} was passed"
            )
        self.graph = graph

    def shortest_path(self, algorithm: str = None, start_node: str = None, end_node: str = None):
        """ Find the shortest path between two nodes in a graph using a specified algorithm """
        if start_node is None:
            raise ValueError("No start node specified")
        if end_node is None:
            raise ValueError("No end node specified")
        if algorithm is None:
            print("No algorithm specified, using Dijkstra's algorithm as default")
        if algorithm == "dijkstra":
            return dc.dijkstra(self.graph, start_node, end_node)
        return None
