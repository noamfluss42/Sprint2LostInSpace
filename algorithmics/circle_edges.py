from utils.coordinate import Coordinate
from enemy.asteroids_zone import AsteroidsZone
from enemy.enemy import Enemy
from enemy.black_hole import BlackHole
from typing import List
from shapely.geometry import Point, LineString, Polygon
from itertools import combinations
import math
from algorithmics.utils.coordinate import Coordinate


def is_legal_edge(c0: Coordinate, c1: Coordinate, enemies: List[Enemy]):
    for enemy in enemies:
        if isinstance(enemy, AsteroidsZone):
            if not is_legal_edge_astroid(c0, c1, enemy):
                return False
        if isinstance(enemy, BlackHole):
            if not is_legal_edge_black_hole(c0, c1, enemy):
                return False
    return True


def is_legal_edge_astroid(c0: Coordinate, c1: Coordinate, zone: AsteroidsZone):
    line = LineString([(c0.x, c0.y), (c1.x, c1.y)])
    poly = Polygon(zone.boundary)
    intersect = isinstance(line.intersection(poly), Point)
    return intersect


def is_legal_edge_black_hole(c0: Coordinate, c1: Coordinate, hole: BlackHole):
    line = LineString([(c0.x, c0.y), (c1.x, c1.y)])
    boundry=[]
    boundry.append(Coordinate(hole.center - hole.radius, hole.center - hole.radius))
    boundry.append(Coordinate(hole.center - hole.radius, hole.center + hole.radius))
    boundry.append(Coordinate(hole.center + hole.radius, hole.center - hole.radius))
    boundry.append(Coordinate(hole.center + hole.radius, hole.center - hole.radius))
    poly = Polygon(boundry)
    intersect = isinstance(line.intersection(poly), Point)
    return intersect
    n=60
    cords_list=[]
    return
    angles = [math.radians(theta) for theta in range(0, 360, 3)]
    cords_list.append([Coordinate((hole.radius+math.sqrt(2))*math.cos(theta), hole.radius+math.sqrt(2)*math.sin(theta)) for theta in angles])
    return cords_list