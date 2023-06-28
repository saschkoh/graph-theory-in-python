# pylint: disable=import-error
"""
This module is used to fullfill the task 5 of the first assignment of the course
"Operations Research" at the Berliner Hochschule fuer Technik (BHT), Department II.
"""
from prettytable import PrettyTable

from oellrich_graph import GraphReader
from dijkstra.core import Dijkstra


def main(
        sources_dict: dict[str, str],
        targets_dict: dict[str, str],
        start: str,
        main_target: str
) -> PrettyTable:
    """
    This function is the main function of this module. It takes a dictionary of source nodes
    and target nodes, the start node name and main target node name as arguments and returns a
    PrettyTable with the results of the iteration measurement series for unmodified and modified
    edge lengths derived from the main target's backward distances.
    """
    source_idx = graph.node_by_name(sources_dict[start]).index
    main_target_idx = graph.node_by_name(targets_dict[main_target]).index
    # initialize table
    title = f"Starknoten {start}"
    table = [["Zielknoten", "Längen c", "Längen c'"]]
    # get backward distances of main target
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
    # read graph and initialize dijkstra
    graph = GraphReader("./graphs/deutschland1.gra", True).read()
    dijkstra = Dijkstra(graph)

    # define source and target nodes
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
    # select source city and get its index
    START = "Stuttgart"
    MAIN_TARGET = "Berlin"

    # run main function
    pretty_table = main(sources, targets, START, MAIN_TARGET)
    print(pretty_table)
