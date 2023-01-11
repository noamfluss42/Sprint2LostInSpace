from typing import List

import networkx as nx

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate


def init_graph(start: Coordinate, end: Coordinate, enemies: List[Enemy]):
    main_graph = nx.Graph()
    main_graph.add_node(start)
    main_graph.add_node(end)
    for enemy in enemies:
        main_graph.add_nodes_from(enemy.get_points())
        for coord in enemy.get_points():
            main_graph.add_edge(start, coord, dist=start.distance_to(coord))
            main_graph.add_edge(coord, end, dist=coord.distance_to(end))
    return main_graph
