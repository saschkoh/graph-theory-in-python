import argparse
import logging
import os
import sys


class Interface:
    def __init__(self):
        self.args = None

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
