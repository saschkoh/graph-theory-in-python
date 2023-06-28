"""
This module contains the unit tests for the Dijsktra class.
"""
from unittest import TestCase
from oellrich_graph import GraphReader

from dijkstra.core import Dijkstra


# global functions to track paths alog the predecessors list
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
        """
        Test test10.gra initialization.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        self.assertEqual(dijkstra.graph.node_count, 10)
        self.assertEqual(dijkstra.graph.edge_count, 32)

    def test_setup_deutschland1(self):
        """
        Test deutschland1.gra initialization.
        """
        dijkstra = Dijkstra(self.test_graphs["deutschland1"])
        self.assertEqual(dijkstra.graph.node_count, 185)
        self.assertEqual(dijkstra.graph.edge_count, 354)

    def test_setup_deutschland2(self):
        """
        Test deutschland2.gra initialization.
        """
        dijkstra = Dijkstra(self.test_graphs["deutschland2"])
        self.assertEqual(dijkstra.graph.node_count, 676)
        self.assertEqual(dijkstra.graph.edge_count, 1107)

    def test_dijkstra_dist_test10_node_a(self):
        """
        Test dijkstra_dist() for test10.gra for node A
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist_a = dijkstra.dijkstra_dist(0)
        self.assertEqual(
            [round(element, 2) for element in dist_a],
            [0, 3.65, 4.24, 2.24, 2.24, 2.41, 1, 1, 1.41, 3.24]
        )

    def test_dijkstra_dist_test10_node_c(self):
        """
        Test dijkstra_dist() for test10.gra for node C
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist_c = dijkstra.dijkstra_dist(2)
        self.assertEqual(
            [round(element, 2) for element in dist_c],
            [3.65, 4.0, 0, 1.41, 2.0, 5.89, 4.65, 4.65, 3.65, 3.0]
        )

    def test_dijkstra_test10_node_a_node_a(self):
        """
        Test dijkstra() for test10.gra for node A to node A.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(0, 0)
        self.assertEqual(round(dist, 2), 0)
        self.assertEqual(track_path(pred, 0, 0), [0])

    def test_dijkstra_test10_node_a_node_b(self):
        """
        Test dijkstra() for test10.gra for node A to node B.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(0, 1)
        self.assertEqual(round(dist, 2), 5.4)
        self.assertEqual(track_path(pred, 0, 1), [0, 3, 1])

    def test_dijkstra_test10_node_a_node_c(self):
        """
        Test dijkstra() for test10.gra for node A to node C.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(0, 2)
        self.assertEqual(round(dist, 2), 3.65)
        self.assertEqual(track_path(pred, 0, 2), [0, 3, 2])

    def test_dijkstra_test10_node_a_node_d(self):
        """
        Test dijkstra() for test10.gra for node A to node D.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(0, 3)
        self.assertEqual(round(dist, 2), 2.24)
        self.assertEqual(track_path(pred, 0, 3), [0, 3])

    def test_dijkstra_test10_node_a_node_e(self):
        """
        Test dijkstra() for test10.gra for node A to node E.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(0, 4)
        self.assertEqual(round(dist, 2), 2.24)
        self.assertEqual(track_path(pred, 0, 4), [0, 4])

    def test_dijkstra_test10_node_a_node_f(self):
        """
        Test dijkstra() for test10.gra for node A to node F.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(0, 5)
        self.assertEqual(round(dist, 2), float('inf'))
        self.assertEqual(track_path(pred, 0, 5), None)

    def test_dijkstra_test10_node_a_node_g(self):
        """
        Test dijkstra() for test10.gra for node A to node G.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(0, 6)
        self.assertEqual(round(dist, 2), 2.41)
        self.assertEqual(track_path(pred, 0, 6), [0, 8, 6])

    def test_dijkstra_test10_node_a_node_h(self):
        """
        Test dijkstra() for test10.gra for node A to node H.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(0, 7)
        self.assertEqual(round(dist, 2), 3.82)
        self.assertEqual(track_path(pred, 0, 7), [0, 8, 6, 7])

    def test_dijkstra_test10_node_a_node_i(self):
        """
        Test dijkstra() for test10.gra for node A to node I.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(0, 8)
        self.assertEqual(round(dist, 2), 1.41)
        self.assertEqual(track_path(pred, 0, 8), [0, 8])

    def test_dijkstra_test10_node_a_node_j(self):
        """
        Test dijkstra() for test10.gra for node A to node J.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(0, 9)
        self.assertEqual(round(dist, 2), 2)
        self.assertEqual(track_path(pred, 0, 9), [0, 9])

    def test_dijkstra_test10_node_a_node_a_dist(self):
        """
        Test dijkstra() for test10.gra for node A to node A with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(0)
        dist, pred = dijkstra.dijkstra(0, 0, back_dist)
        self.assertEqual(round(dist, 2), 0)
        self.assertEqual(track_path(pred, 0, 0), [0])

    def test_dijkstra_test10_node_a_node_b_dist(self):
        """
        Test dijkstra() for test10.gra for node A to node B with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(1)
        dist, pred = dijkstra.dijkstra(0, 1, back_dist)
        self.assertEqual(round(dist, 2), 5.4)
        self.assertEqual(track_path(pred, 0, 1), [0, 3, 1])

    def test_dijkstra_test10_node_a_node_c_dist(self):
        """
        Test dijkstra() for test10.gra for node A to node C with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(2)
        dist, pred = dijkstra.dijkstra(0, 2, back_dist)
        self.assertEqual(round(dist, 2), 3.65)
        self.assertEqual(track_path(pred, 0, 2), [0, 3, 2])

    def test_dijkstra_test10_node_a_node_d_dist(self):
        """
        Test dijkstra() for test10.gra for node A to node D with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(3)
        dist, pred = dijkstra.dijkstra(0, 3, back_dist)
        self.assertEqual(round(dist, 2), 2.24)
        self.assertEqual(track_path(pred, 0, 3), [0, 3])

    def test_dijkstra_test10_node_a_node_e_dist(self):
        """
        Test dijkstra() for test10.gra for node A to node E with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(4)
        dist, pred = dijkstra.dijkstra(0, 4, back_dist)
        self.assertEqual(round(dist, 2), 2.24)
        self.assertEqual(track_path(pred, 0, 4), [0, 4])

    def test_dijkstra_test10_node_a_node_f_dist(self):
        """
        Test dijkstra() for test10.gra for node A to node F with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(5)
        dist, pred = dijkstra.dijkstra(0, 5, back_dist)
        self.assertEqual(round(dist, 2), float('inf'))
        self.assertEqual(track_path(pred, 0, 5), None)

    def test_dijkstra_test10_node_a_node_g_dist(self):
        """
        Test dijkstra() for test10.gra for node A to node G with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(6)
        dist, pred = dijkstra.dijkstra(0, 6, back_dist)
        self.assertEqual(round(dist, 2), 2.41)
        self.assertEqual(track_path(pred, 0, 6), [0, 8, 6])

    def test_dijkstra_test10_node_a_node_h_dist(self):
        """
        Test dijkstra() for test10.gra for node A to node H with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(7)
        dist, pred = dijkstra.dijkstra(0, 7, back_dist)
        self.assertEqual(round(dist, 2), 3.82)
        self.assertEqual(track_path(pred, 0, 7), [0, 8, 6, 7])

    def test_dijkstra_test10_node_a_node_i_dist(self):
        """
        Test dijkstra() for test10.gra for node A to node I with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(8)
        dist, pred = dijkstra.dijkstra(0, 8, back_dist)
        self.assertEqual(round(dist, 2), 1.41)
        self.assertEqual(track_path(pred, 0, 8), [0, 8])

    def test_dijkstra_test10_node_a_node_j_dist(self):
        """
        Test dijkstra() for test10.gra for node A to node J with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(9)
        dist, pred = dijkstra.dijkstra(0, 9, back_dist)
        self.assertEqual(round(dist, 2), 2)
        self.assertEqual(track_path(pred, 0, 9), [0, 9])

    def test_dijkstra_test10_node_f_node_a(self):
        """
        Test dijkstra() for test10.gra for node F to node A.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(5, 0)
        self.assertEqual(round(dist, 2), 2.41)
        self.assertEqual(track_path(pred, 5, 0), [5, 6, 0])

    def test_dijkstra_test10_node_f_node_b(self):
        """
        Test dijkstra() for test10.gra for node F to node B.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(5, 1)
        self.assertEqual(round(dist, 2), 3)
        self.assertEqual(track_path(pred, 5, 1), [5, 1])

    def test_dijkstra_test10_node_f_node_c(self):
        """
        Test dijkstra() for test10.gra for node F to node C.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(5, 2)
        self.assertEqual(round(dist, 2), 5.89)
        self.assertEqual(track_path(pred, 5, 2), [5, 8, 3, 2])

    def test_dijkstra_test10_node_f_node_d(self):
        """
        Test dijkstra() for test10.gra for node F to node D.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(5, 3)
        self.assertEqual(round(dist, 2), 4.48)
        self.assertEqual(track_path(pred, 5, 3), [5, 8, 3])

    def test_dijkstra_test10_node_f_node_e(self):
        """
        Test dijkstra() for test10.gra for node F to node E.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(5, 4)
        self.assertEqual(round(dist, 2), 4.65)
        self.assertEqual(track_path(pred, 5, 4), [5, 6, 0, 4])

    def test_dijkstra_test10_node_f_node_f(self):
        """
        Test dijkstra() for test10.gra for node F to node F.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(5, 5)
        self.assertEqual(round(dist, 2), 0)
        self.assertEqual(track_path(pred, 5, 5), [5])

    def test_dijkstra_test10_node_f_node_g(self):
        """
        Test dijkstra() for test10.gra for node F to node G.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(5, 6)
        self.assertEqual(round(dist, 2), 1.41)
        self.assertEqual(track_path(pred, 5, 6), [5, 6])

    def test_dijkstra_test10_node_f_node_h(self):
        """
        Test dijkstra() for test10.gra for node F to node H.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(5, 7)
        self.assertEqual(round(dist, 2), 2)
        self.assertEqual(track_path(pred, 5, 7), [5, 7])

    def test_dijkstra_test10_node_f_node_i(self):
        """
        Test dijkstra() for test10.gra for node F to node I.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(5, 8)
        self.assertEqual(round(dist, 2), 2.24)
        self.assertEqual(track_path(pred, 5, 8), [5, 8])

    def test_dijkstra_test10_node_f_node_j(self):
        """
        Test dijkstra() for test10.gra for node F to node J.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        dist, pred = dijkstra.dijkstra(5, 9)
        self.assertEqual(round(dist, 2), 4.24)
        self.assertEqual(track_path(pred, 5, 9), [5, 7, 9])

    def test_dijkstra_test10_node_f_node_a_dist(self):
        """
        Test dijkstra() for test10.gra for node F to node A with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(0)
        dist, pred = dijkstra.dijkstra(5, 0, back_dist)
        self.assertEqual(round(dist, 2), 2.41)
        self.assertEqual(track_path(pred, 5, 0), [5, 6, 0])

    def test_dijkstra_test10_node_f_node_b_dist(self):
        """
        Test dijkstra() for test10.gra for node F to node B with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(1)
        dist, pred = dijkstra.dijkstra(5, 1, back_dist)
        self.assertEqual(round(dist, 2), 3)
        self.assertEqual(track_path(pred, 5, 1), [5, 1])

    def test_dijkstra_test10_node_f_node_c_dist(self):
        """
        Test dijkstra() for test10.gra for node F to node C with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(2)
        dist, pred = dijkstra.dijkstra(5, 2, back_dist)
        self.assertEqual(round(dist, 2), 5.89)
        self.assertEqual(track_path(pred, 5, 2), [5, 8, 3, 2])

    def test_dijkstra_test10_node_f_node_d_dist(self):
        """
        Test dijkstra() for test10.gra for node F to node D with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(3)
        dist, pred = dijkstra.dijkstra(5, 3, back_dist)
        self.assertEqual(round(dist, 2), 4.48)
        self.assertEqual(track_path(pred, 5, 3), [5, 8, 3])

    def test_dijkstra_test10_node_f_node_e_dist(self):
        """
        Test dijkstra() for test10.gra for node F to node E with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(4)
        dist, pred = dijkstra.dijkstra(5, 4, back_dist)
        self.assertEqual(round(dist, 2), 4.65)
        self.assertEqual(track_path(pred, 5, 4), [5, 6, 0, 4])

    def test_dijkstra_test10_node_f_node_f_dist(self):
        """
        Test dijkstra() for test10.gra for node F to node F with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(5)
        dist, pred = dijkstra.dijkstra(5, 5, back_dist)
        self.assertEqual(round(dist, 2), 0)
        self.assertEqual(track_path(pred, 5, 5), [5])

    def test_dijkstra_test10_node_f_node_g_dist(self):
        """
        Test dijkstra() for test10.gra for node F to node G with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(6)
        dist, pred = dijkstra.dijkstra(5, 6, back_dist)
        self.assertEqual(round(dist, 2), 1.41)
        self.assertEqual(track_path(pred, 5, 6), [5, 6])

    def test_dijkstra_test10_node_f_node_h_dist(self):
        """
        Test dijkstra() for test10.gra for node F to node H with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(7)
        dist, pred = dijkstra.dijkstra(5, 7, back_dist)
        self.assertEqual(round(dist, 2), 2)
        self.assertEqual(track_path(pred, 5, 7), [5, 7])

    def test_dijkstra_test10_node_f_node_i_dist(self):
        """
        Test dijkstra() for test10.gra for node F to node I with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(8)
        dist, pred = dijkstra.dijkstra(5, 8, back_dist)
        self.assertEqual(round(dist, 2), 2.24)
        self.assertEqual(track_path(pred, 5, 8), [5, 8])

    def test_dijkstra_test10_node_f_node_j_dist(self):
        """
        Test dijkstra() for test10.gra for node F to node J with dist.
        """
        dijkstra = Dijkstra(self.test_graphs["test10"])
        back_dist = dijkstra.dijkstra_dist(9)
        dist, pred = dijkstra.dijkstra(5, 9, back_dist)
        self.assertEqual(round(dist, 2), 4.24)
        self.assertEqual(track_path(pred, 5, 9), [5, 7, 9])
