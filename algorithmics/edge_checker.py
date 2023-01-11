from utils.coordinate import Coordinate
from enemy.asteroids_zone import AsteroidsZone

from shapely.geometry import Point, LineString, Polygon


def is_legal_edge(c0: Coordinate, c1: Coordinate, enemies):
    pass


def is_legal_edge_astroid(c0: Coordinate, c1: Coordinate, zone: AsteroidsZone):
    line = LineString([(c0.x, c0.y), (c1.x, c1.y)])
    poly = Polygon(zone.boundary)


