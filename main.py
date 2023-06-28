"""
This module is the main module that is being used to fullfill the tasks from the first assignment
in the course "Operations Research" at the Berliner Hochschule fuer Technik (BHT), Department II.
It uses the Python implementation of a Graph class by Sascha Thiede and Sascha Kohler which is
based on the Graph class implementation in C++ by Prof. Martin Oellrich, the lecturer of the course.

The task was to implement Dijkstra's algorithm for finding shortest paths in a graph. The algorithm
was implemented in the Dijkstra class in the core module.
Author: Sascha Kohler
"""
from oellrich_graph import GraphReader, Node
from dijkstra.core import Dijkstra


# global functions to track paths alog the predecessors list and print them
def track_path(predecessors: list[int], source_idx: int, target_idx: int):
    """
    This function tracks a path from source index to target index from its calculated predecessors
    list and returns a list of node indices in the logical order of the path from source to target.
    """
    path = []
    current_idx = target_idx
    if predecessors[current_idx] is not None:
        while current_idx != source_idx:
            path.append(current_idx)
            current_idx = predecessors[current_idx]
        path.append(predecessors[source_idx])
        path = path[::-1]
        return path
    return None


def print_path(path: list[Node], dist: float):
    """
    This function prints a path if nodes and its distance.
    """
    path_strings = [node.name for node in path]
    print(f"[{round(dist, 2):<4}]: {' -> '.join(path_strings)}")


class TasksTest10:
    """
    This class contains the tasks for the test10 graph.
    """
    def __init__(self):
        self.graph = GraphReader("./graphs/test10.gra", True).read()
        self.dijkstra = Dijkstra(self.graph)

    def task_2(self, target_names: list[str] = ["A", "C"]):
        """
        This function prints the backward distances for the nodes in the target_names list.
        """
        for node in self.dijkstra.graph.nodes:
            if node.name in target_names:
                print(f"\nBackward distances node of {node.name}")
                dist = self.dijkstra.dijkstra_dist(node.index)
                for i, dist in enumerate(dist):
                    print(f" {i}: {self.dijkstra.graph.nodes[i].name} [{round(dist, 2):<4}]")

    def task_3_4(self, source_names: list[str] = ["A", "C", "F"], compare: bool = False):
        """
        This function prints all the shortest paths trees for the nodes in the source_names list
        without backward distances and with backward distances to visually compare if equal.
        """
        for source_node in self.dijkstra.graph.nodes:
            if source_node.name in source_names:
                print(f"\nNode {source_node.name}: Shortest paths tree of without backward distances")
                self.compute_paths(source_node)
                if compare:
                    print(f"\nNode {source_node.name}: Shortest paths tree of with backward distances")
                    self.compute_paths(source_node, True)

    def compute_paths(self, source_node: Node, modified: bool = False):
        """
        This method computes the shortest paths tree for a given source node and prints the paths.
        """
        for target_node in self.dijkstra.graph.nodes:
            if target_node.index != source_node.index:
                if modified:
                    back_dist = self.dijkstra.dijkstra_dist(target_node.index)
                    dist, predecessors = self.dijkstra.dijkstra(source_node.index, target_node.index, back_dist)
                else:
                    dist, predecessors = self.dijkstra.dijkstra(source_node.index, target_node.index)
                index_path = track_path(predecessors, source_node.index, target_node.index)
                if index_path is not None:
                    path = [self.dijkstra.graph.nodes[index] for index in index_path]
                    print_path(path, dist)


if __name__ == "__main__":
    # test10.gra tasks
    test_test10 = TasksTest10()
    # insert test set as list of node names
    # default test set is ["A", "C"]
    test_test10.task_2()
    # default test set is ["A", "C", "F"], compare with modified algo with compare=True
    test_test10.task_3_4(compare=True)
    





