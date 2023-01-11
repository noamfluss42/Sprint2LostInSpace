from utils.coordinate import Coordinate
from enemy.asteroids_zone import AsteroidsZone
from enemy.enemy import Enemy
from enemy.black_hole import BlackHole
from typing import List

from shapely.geometry import Point, LineString, Polygon


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

    intersect = line.intersects(poly)
    return intersect


def is_legal_edge_black_hole(c0: Coordinate, c1: Coordinate, hole: BlackHole):
    line = LineString([(c0.x, c0.y), (c1.x, c1.y)])
    circle = Point(hole.center.x, hole.center.y).buffer(hole.radius)

    return line.intersects(circle)
