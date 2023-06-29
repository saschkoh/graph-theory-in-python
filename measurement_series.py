"""
This module is used to fullfill the task 5 of the first assignment in the course
"Operations Research" at Berliner Hochschule fuer Technik (BHT), Department II.
"""
from prettytable import PrettyTable
from oellrich_graph import GraphReader

from dijkstra.core import Dijkstra


def main(
        graph_string: str,
        start: str,
        main_target: str,
        sources_dict: dict[str: str],
        targets_dict: dict[str: str]
) -> PrettyTable:
    """
    This function is the main function of this module. It takes the graph's file path, the start
    node name and main target node name and the corresponding source and target dictionaries as
    arguments and returns a PrettyTable with the results of the iteration measurement series for
    unmodified and modified edge lengths derived from the main target's backward distances.
    """
    graph = GraphReader(graph_string, True).read()
    source_idx = graph.node_by_name(sources_dict[start]).index
    main_target_idx = graph.node_by_name(targets_dict[main_target]).index
    # initialize table
    title = f"Starknoten {start}"
    table = [["Zielknoten", "Längen c", "Längen c'"]]
    # get backward distances of main target
    dijkstra = Dijkstra(graph)
    back_dist = dijkstra.dijkstra_dist(main_target_idx)
    # iterate over all target nodes and write to row
    for key in targets:
        target_idx = graph.node_by_name(targets[key]).index
        # without backward distances
        _, _, iter_1 = dijkstra.dijkstra(
            source_idx,
            target_idx,
            count=True
        )
        # with backward distances
        _, _, iter_2 = dijkstra.dijkstra(
            source_idx,
            target_idx,
            back_dist,
            True
        )
        # write row
        table.append([key, iter_1, iter_2])
    # print table
    tab = PrettyTable(table[0])
    tab.title = title
    tab.add_rows(table[1:])
    return tab


if __name__ == "__main__":
    # define graph paths, source and target nodes
    graphs = {
        1: "./test/test-graphs/deutschland1.gra",
        2: "./test/test-graphs/deutschland2.gra"
    }
    sources = {
        "Stuttgart": "711000"
    }
    targets = {
        "Berlin": "300000",
        "Potsdam": "331000",
        "Nauen": "332100",
        "Oranienburg": "330100",
        "Strausberg": "334100",
        "Fürstenwalde": "336100",
        "Zeuthen": "337620",
        "Michendorf": "332050"
    }
    # select graph path, source city and main target city
    GRAPH = graphs[2]
    START = "Stuttgart"
    MAIN_TARGET = "Berlin"
    # run main function and print table
    pretty_table = main(GRAPH, START, MAIN_TARGET, sources, targets)
    print(pretty_table)

    # output:
    # measurement series for deutschland1.gra
    # +-------------------------------------+
    # |         Starknoten Stuttgart        |
    # +--------------+----------+-----------+
    # |  Zielknoten  | Längen c | Längen c' |
    # +--------------+----------+-----------+
    # |    Berlin    |   183    |     17    |
    # |   Potsdam    |   178    |     16    |
    # |    Nauen     |   184    |     31    |
    # | Oranienburg  |   202    |     55    |
    # |  Strausberg  |   209    |     57    |
    # | Fürstenwalde |   201    |     78    |
    # |   Zeuthen    |   182    |     29    |
    # |  Michendorf  |   175    |     15    |
    # +--------------+----------+-----------+

    # measurement series for deutschland2.gra
    # +-------------------------------------+
    # |         Starknoten Stuttgart        |
    # +--------------+----------+-----------+
    # |  Zielknoten  | Längen c | Längen c' |
    # +--------------+----------+-----------+
    # |    Berlin    |   649    |     14    |
    # |   Potsdam    |   629    |     13    |
    # |    Nauen     |   653    |     87    |
    # | Oranienburg  |   677    |    144    |
    # |  Strausberg  |   681    |    191    |
    # | Fürstenwalde |   684    |    248    |
    # |   Zeuthen    |   657    |     74    |
    # |  Michendorf  |   639    |     32    |
    # +--------------+----------+-----------+
