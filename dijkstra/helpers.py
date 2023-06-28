"""
This module contains helper functions for the Dijkstra algorithm and unit tests.
"""


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
