import math

import numpy as np

from algorithmics.enemy.radar import Radar
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
        if "Radar" in str(type(enemy)):
           if not is_legal_edge_radar(c0, c1, enemy):
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

            return True
    if (c0 == boundary[-1] and c1 == boundary[0]) or (c1 == boundary[-1] and c0 == boundary[0]):

        return True
    return False

def is_legal_edge_black_hole(c0: Coordinate, c1: Coordinate, hole: BlackHole):
    line = LineString([(c0.x, c0.y), (c1.x, c1.y)])
    circle = Point(hole.center.x, hole.center.y).buffer(hole.radius)
    return not line.intersects(circle)


def is_legal_edge_radar(c0: Coordinate, c1: Coordinate, radar: Radar):
    if is_two_points_path_valid(c0, c1, radar.center, radar.radius):
        return True
    return False


def is_two_points_path_valid(point1, point2, center, radius):
    line = LineString([(point1.x, point1.y), (point2.x, point2.y)])
    circle = Point(center.x, center.y).buffer(radius)
    """print("point1, point2",point1, point2)
    print("line.intersects(circle)",line.intersects(circle))
    print()
    print("circle.intersection(line)",circle.intersection(line))"""
    intersection = circle.intersection(line)

    if not circle.intersects(line) or "Point" in str(type(intersection)):
        return True
    else:
        point1, point2 = intersection.boundary
    # first angle
    center_angle1 = np.arctan2(center.y - point1.y, center.x - point1.x)
    points_angle1 = np.arctan2(point2.y - point1.y, point2.x - point1.x)
    angle1 = abs(center_angle1 - points_angle1)
    # second angle
    center_angle2 = np.arctan2(center.y - point2.y, center.x - point2.x)
    points_angle2 = np.arctan2(point1.y - point2.y, point1.x - point2.x)
    angle2 = abs(center_angle2 - points_angle2)

    if math.pi / 4 <= angle1 <= 3 * math.pi / 4 and math.pi / 4 <= angle2 <= 3 * math.pi / 4:
        return True
    else:
        return False

#points_array = [Coordinate(-5,0), Coordinate(0,-15),Coordinate(20, -25), Coordinate(35,-25), Coordinate(50,0)]

#for i in range(0, len(points_array)-1):
    # print(is_two_points_path_valid(points_array[i], points_array[i+1], Coordinate(30,0), 35))4


"""circle = Point(10, -10).buffer(5)
p1 = Coordinate(0,0)
p2 = Coordinate(20,0)
l = LineString([(p1.x, p1.y), (p2.x, p2.y)])
print(Coordinate(3,0).boundary)
"""
