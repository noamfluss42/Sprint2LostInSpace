from typing import List, Tuple

import networkx as nx

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils import create_graph
from algorithmics.utils.coordinate import Coordinate



def calculate_path(source: Coordinate, targets: List[Coordinate], enemies: List[Enemy]):
    main_graph = create_graph.init_graph(source, targets, enemies)
    end_dummy_node = Coordinate(0, 0)
    start_dummy_node = Coordinate(0, 0)
    targets_graph = nx.Graph()
    targets_graph.add_node(source)
    targets_graph.add_nodes_from(targets)
    # targets_graph.add_edge(start_dummy_node, source, weight=0)
    # print("here")
    for i in range(len(targets)):
        path_from_start = nx.shortest_path(main_graph, source=source,
                                           target=targets[i], weight='dist')
        targets_graph.add_edge(source, targets[i],
                               dist=source.distance_to(targets[i]))
        targets_graph.add_edge(targets[i], source,
                               dist=source.distance_to(targets[i]))
        print(f"source to targets[{i}]",source.distance_to(targets[i]))#path_length(path_from_start))
        for j in range(i+1, len(targets)):
            targets_graph.add_edge(targets[i], targets[j],
                                   dist=targets[i].distance_to(targets[j]))
            targets_graph.add_edge(targets[j], targets[i],
                                   dist=targets[i].distance_to(targets[j]))
            print(f"{targets[i]}, {targets[j]}, targets{i} to targets{j}",targets[i].distance_to(targets[j]))
            # path_from_start = nx.shortest_path(main_graph, source=source, target=targets[i], weight='dist')
            # targets_graph.add_edge(source, targets[i], dist=path_length(path_from_start))
            # print(i, path_length(path_from_start))
            # # targets_graph.add_edge(targets[i], source, dist=path_length(path_from_start))
            # # targets_graph.add_edge(targets[i], end_dummy_node, weight=0)
            # for j in range(i + 1, len(targets)):
            #     path_to_next_target = nx.shortest_path(main_graph, source=targets[i], target=targets[j], weight='dist')
            #     targets_graph.add_edge(targets[i], targets[j], weight=path_length(path_to_next_target))
            #     # targets_graph.add_edge(targets[j], targets[i], weight=path_length(path_to_next_target))
    print("targets_graph",targets_graph)
    # path = nx.approximation.simulated_annealing_tsp(targets_graph, list(targets_graph) + [next(iter(targets_graph))], source=source)
    path = travellingSalesmanProblem(nx.adjacency_matrix(targets_graph, weight='dist'), source)
    print(path)
    return [source] + targets, main_graph


def path_length(path):
    total = 0
    for i in range(len(path) - 1):
        total += path[i].distance_to(path[i+1])
    return total


# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations

V = 3


# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path