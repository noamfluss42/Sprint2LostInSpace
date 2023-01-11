from typing import List, Tuple

import networkx as nx

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils import create_graph
from algorithmics.utils.coordinate import Coordinate


# Navigator


def calculate_path(source: Coordinate, targets: List[Coordinate], enemies: List[Enemy], allowed_detection: float = 0) \
        -> Tuple[List[Coordinate], nx.Graph]:
    """Calculates a path from source to target without any detection

    Note: The path must start at the source coordinate and end at the target coordinate!

    :param source: source coordinate of the spaceship
    :param targets: target coordinate of the spaceship
    :param enemies: list of enemies along the way
    :param allowed_detection: maximum allowed distance of radar detection
    :return: list of calculated path waypoints and the graph constructed
    """
    #source = Coordinate(50, 1)
    main_graph = create_graph.init_graph(source, targets[0], enemies)
    print("source",source)
    print("targets[0]",targets[0])

    path = nx.shortest_path(main_graph, source=source, target=targets[0], weight='dist')
    #path = [source,Coordinate(-5,0), Coordinate(0,-15),Coordinate(20, -25), Coordinate(45,-24), targets[0]]
    return path, main_graph

