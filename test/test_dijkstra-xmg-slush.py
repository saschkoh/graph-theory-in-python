"""
This module contains the unit tests for the Dijsktra class.
"""
from unittest import TestCase
import numpy as np

from dijkstra.core import Dijkstra
from oellrich_graph import GraphReader


class TestDijkstra(TestCase):
    """
    This class is the TestCase for the Dijkstra class.
    """
    # read the test graphs from file and initialize the neighbors
    test_graphs = {
        "test10": GraphReader("./graphs/test10.gra", True).read(),
        "deutschland1": GraphReader("./graphs/deutschland1.gra", True).read(),
        "deutschland2": GraphReader("./graphs/deutschland2.gra", True).read(),
    }

    def test_setup_test10(self):
        dijkstra = Dijkstra(self.test_graphs["test10"])
        self.assertEqual(dijkstra.graph.node_count, 10)
        self.assertEqual(dijkstra.graph.edge_count, 32)

    def test_setup_deutschland1(self):
        dijkstra = Dijkstra(self.test_graphs["deutschland1"])
        self.assertEqual(dijkstra.graph.node_count, 185)
        self.assertEqual(dijkstra.graph.edge_count, 354)

    def test_setup_deutschland2(self):
        dijkstra = Dijkstra(self.test_graphs["deutschland2"])
        self.assertEqual(dijkstra.graph.node_count, 676)
        self.assertEqual(dijkstra.graph.edge_count, 1107)

    def test_dijkstra_dist_test10(self):
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist_a = dijkstra.dijkstra_dist(0)
        dist_c = dijkstra.dijkstra_dist(2)
        self.assertEqual(
            [round(element, 2) for element in dist_a],
            [0, 3.65, 4.24, 2.24, 2.24, 2.41, 1, 1, 1.41, 3.24]
        )
        self.assertEqual(
            [round(element, 2) for element in dist_c],
            [3.65, 4.0, 0, 1.41, 2.0, 5.89, 4.65, 4.65, 3.65, 3.0]
        )
