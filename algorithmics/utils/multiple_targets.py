from typing import List, Tuple

import networkx as nx

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils import create_graph
from algorithmics.utils.coordinate import Coordinate


def calculate_path(source: Coordinate, targets: List[Coordinate], enemies: List[Enemy]):
    main_graph = create_graph.init_graph(source, targets, enemies)
    targets = targets[:3]
    end_dummy_node = Coordinate(0, 0)
    start_dummy_node = Coordinate(0, 0)
    targets_graph = nx.Graph()
    targets_graph.add_node(source)
    targets_graph.add_nodes_from(targets)
    # targets_graph.add_edge(start_dummy_node, source, weight=0)
    print("here")
    for i in range(len(targets)):
        path_from_start = nx.shortest_path(main_graph, source=source, target=targets[i], weight='dist')
        print("start", i)
        targets_graph.add_edge(source, targets[i], dist=path_length(path_from_start))
        print(i, path_length(path_from_start))
        # targets_graph.add_edge(targets[i], source, dist=path_length(path_from_start))
        # targets_graph.add_edge(targets[i], end_dummy_node, weight=0)
        for j in range(i + 1, len(targets)):
            path_to_next_target = nx.shortest_path(main_graph, source=targets[i], target=targets[j], weight='dist')
            print("resume", i, j)
            targets_graph.add_edge(targets[i], targets[j], weight=path_length(path_to_next_target))
            print(i, j, path_length(path_to_next_target))
            # targets_graph.add_edge(targets[j], targets[i], weight=path_length(path_to_next_target))
    print("exit")
    path = nx.approximation.traveling_salesman_problem(targets_graph)
    print("after")
    print(path)
    return [source] + path, main_graph


def path_length(path):
    total = 0
    for i in range(len(path) - 1):
        total += path[i].distance_to(path[i+1])
    return total
