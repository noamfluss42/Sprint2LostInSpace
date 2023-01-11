from typing import List

import networkx as nx

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate


def init_graph(start: Coordinate, end: Coordinate, enemies: List[Enemy]):
    main_graph = nx.Graph()
    main_graph.add_edge(start)
    main_graph.add_edge(end)
    main_graph.add_edge(start, end, dist=start.distance_to(end))
    for enemy in enemies:
        main_graph.add_nodes_from(enemy.get_points())
    return main_graph
