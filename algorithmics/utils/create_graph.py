from typing import List

import networkx as nx

from algorithmics import edge_checker, create_legal_edges
from algorithmics.enemy.asteroids_zone import AsteroidsZone
from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate


def init_graph(start: Coordinate, end: Coordinate, enemies: List):
    main_graph = nx.Graph()
    main_graph.add_node(start)
    main_graph.add_node(end)
    for enemy in enemies:
        main_graph.add_nodes_from(enemy.get_points())
    create_legal_edges.get_legal_edges(main_graph, enemies)
    return main_graph
