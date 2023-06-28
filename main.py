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


# global functions to track paths along the predecessors list and print them
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


if __name__ == "__main__":

