import networkx as nx
from itertools import combinations
import math
from algorithmics.utils.coordinate import Coordinate
import edge_checker



def get_legal_edges(graph, enemies):
    for start, end in combinations(graph.nodes, 2):
        if edge_checker.is_legal_edge(start, end, enemies):
            graph.add_edge(start, end)
