import argparse
import os

from oellrich_graph import GraphReader
from core import Dijkstra


# global function to track paths along the predecessors list
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


class Interface:
    """
    CLI for the Dijkstra algorithm implementation.
    """
    def __init__(self):
        self.args = None
        self.graph = None
        self.dijkstra = None
        self.pred = None
        self.source_idx = None
        self.target_idx = None
        self.dist = None
        self.pred = None
        self.iter = None

    def parse_args(self):
        """
        This method parses the command line arguments and returns the input file name.
        """
        parser = argparse.ArgumentParser(
            description="Read graphs and find shortest paths using Dijkstra's algorithm"
        )
        parser.add_argument(
            "input_file",
            nargs="?",
            type=str,
            help="path to the input file",
        )
        parser.add_argument(
            "-s",
            "--source",
            nargs="?",
            type=str,
            help="source node name",
        )
        parser.add_argument(
            "-t",
            "--target",
            nargs="?",
            type=str,
            help="target node name",
        )
        parser.add_argument(
            "-m",
            "--mode",
            nargs="?",
            type=int,
            help="use unmodified or modified edge weigths (1-2)",
            required=False,
            default=2
        )
        parser.add_argument(
            "-pr",
            "--predecessors",
            help="print the predecessors",
            action="store_true",
        )
        parser.add_argument(
            "-pa",
            "--path",
            help="print the path",
            action="store_true",
        )
        self.args = vars(parser.parse_args())

    def check_input_path(self):
        """
        This method checks if the input path is valid.
        """
        if self.args["input_file"] is not None:
            if os.path.exists(self.args["input_file"]):
                if self.args["input_file"].endswith(".gra"):
                    pass
                else:
                    raise ValueError("Input file must be a .gra file")
        else:
            raise FileNotFoundError(f"File {self.args['input_file']} not found")

    def check_st(self):
        """
        This method checks if the source and target nodes are specified.
        """
        if self.args["source"] is None:
            raise ValueError("Source node must be specified")
        elif self.args["target"] is None:
            raise ValueError("Target node must be specified")

    def check_mode(self):
        """
        This method checks if the mode input is valid.
        """
        if self.args["mode"] in [1, 2]:
            pass
        else:
            raise ValueError("Mode must be 1 or 2")

    def init_dijkstra(self):
        """
        This method initializes the Dijkstra class object with the graph.
        """
        self.graph = GraphReader(self.args["input_file"], True).read()
        self.dijkstra = Dijkstra(self.graph)
        self.source_idx = self.graph.node_by_name(self.args["source"]).index
        self.target_idx = self.graph.node_by_name(self.args["target"]).index

    def print_path(self):
        """
        This method prints a path if nodes and its distance.
        """
        index_path = track_path(self.pred, self.source_idx, self.target_idx)
        path_strings = [self.graph.nodes[index].name for index in index_path]
        print(f"path: {' -> '.join(path_strings)}")

    def run(self):
        """
        This method runs the program.
        """
        self.parse_args()
        self.check_st()
        self.check_mode()
        self.init_dijkstra()
        if self.args["mode"] == 1:
            print("\nUsing mode 1: unmodified edge weights")
            self.dist, self.pred, self.iter = self.dijkstra.dijkstra(self.source_idx, self.target_idx, count=True)
        elif self.args["mode"] == 2:
            print("\nUsing mode 2: modified edge weights")
            back_dist = self.dijkstra.dijkstra_dist(self.target_idx)
            self.dist, self.pred, self.iter = self.dijkstra.dijkstra(self.source_idx, self.target_idx, back_dist, count=True)
        print(f"s -> t shortest path: {self.dist}")
        print(f"iterations: {self.iter}")
        if self.args["predecessors"]:
            print(f"predecessors: {self.pred}")
        if self.args["path"]:
            self.print_path()


def main():
    Interface().run()


if __name__ == "__main__":
    main()
