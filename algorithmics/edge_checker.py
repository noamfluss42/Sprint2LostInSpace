from utils.coordinate import Coordinate
from enemy.asteroids_zone import AsteroidsZone
from enemy.enemy import Enemy
from enemy.black_hole import BlackHole
from typing import List

from shapely.geometry import Point, LineString, Polygon


def is_legal_edge(c0: Coordinate, c1: Coordinate, enemies: List[Enemy]):
    for enemy in enemies:
        if "AsteroidsZone" in str(type(enemy)):
            if not is_legal_edge_astroid(c0, c1, enemy):
                return False
        if "BlackHole" in str(type(enemy)):
            if not is_legal_edge_black_hole(c0, c1, enemy):
                return False
    return True

def is_legal_edge_astroid(c0: Coordinate, c1: Coordinate, zone: AsteroidsZone):
    line = LineString([(c0.x, c0.y), (c1.x, c1.y)])

    poly = Polygon([(c.x, c.y) for c in zone.boundary])
    if not line.intersects(poly):
        return True
    if c0 not in zone.boundary and c1 in zone.boundary:
        return "LineString" not in str(type(line.intersection(poly)))
    if c0 in zone.boundary and c1 not in zone.boundary:
        return "LineString" not in str(type(line.intersection(poly)))

    # return False
    #
    boundary = zone.boundary
    for i in range(len(boundary) - 1):
        if (c0 == boundary[i] and c1 == boundary[i+1]) or (c0 == boundary[i+1] and c1 == boundary[i]):
            print(line, "True")
            return True
    if (c0 == boundary[-1] and c1 == boundary[0]) or (c1 == boundary[-1] and c0 == boundary[0]):
        print(line, "True")
        return True
    return False


def is_legal_edge_black_hole(c0: Coordinate, c1: Coordinate, hole: BlackHole):
    line = LineString([(c0.x, c0.y), (c1.x, c1.y)])
    circle = Point(hole.center.x, hole.center.y).buffer(hole.radius)
    return not line.intersects(circle)
