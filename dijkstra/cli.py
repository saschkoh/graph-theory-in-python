import argparse
import os

from oellrich_graph import GraphReader
from core import Dijkstra
from helpers import track_path


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
            default=None
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
            "--modified",
            help="use modified edge weigths",
            action="store_true"
        )
        parser.add_argument(
            "-i",
            "--iter",
            help="print the number of iterations",
            action="store_true",
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

    def check_t(self):
        """
        This method checks if the target nodes are specified.
        """
        if self.args["target"] is None:
            raise ValueError("Target node must be specified")

    def init_dijkstra(self):
        """
        This method initializes the Dijkstra class object with the graph.
        """
        self.graph = GraphReader(self.args["input_file"], True).read()
        self.dijkstra = Dijkstra(self.graph)
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
        self.check_t()
        self.init_dijkstra()
        if self.args["source"] is None:
            print("\nUsing mode 0: only backward distances")
            back_dist = self.dijkstra.dijkstra_dist(self.target_idx)
            print(f"backward distances: {back_dist}")
        else:
            self.source_idx = self.graph.node_by_name(self.args["source"]).index
            if self.args["modified"]:
                print("\nUsing mode 1: modified edge weights")
                back_dist = self.dijkstra.dijkstra_dist(self.target_idx)
                self.dist, self.pred, self.iter = self.dijkstra.dijkstra(
                    self.source_idx, self.target_idx, back_dist, count=True
                )
            else:
                print("\nUsing mode 2: unmodified edge weights")
                self.dist, self.pred, self.iter = self.dijkstra.dijkstra(
                    self.source_idx, self.target_idx, count=True
                )
            if self.dist is not float("inf"):
                print(f"s -> t shortest path: {self.dist}")
                if self.args["iter"]:
                    print(f"iterations: {self.iter}")
                if self.args["predecessors"]:
                    print(f"predecessors: {self.pred}")
                if self.args["path"]:
                    self.print_path()
            else:
                print("No path found")


def main():
    Interface().run()


if __name__ == "__main__":
    main()
