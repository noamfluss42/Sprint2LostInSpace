import math
from typing import List

import numpy as np

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate


def get_bounding_circle(center, radius, point_count):
    angles = [math.radians(theta) for theta in range(0, 360, 360 // point_count)]
    return [Coordinate(center.x + radius * math.cos(theta), center.y + radius * math.sin(theta)) for
            theta in angles]


class Radar(Enemy):

    def __init__(self, center: Coordinate, radius: float):
        """Initializes a radar object at the location with the given detection radius

        :param center: location of the radar
        :param radius: detection radius of the radar
        """
        self.center = center
        self.radius = radius

    def get_points(self) -> List[Coordinate]:
        points = []
        min_radius = 1
        jump = 1
        for r in np.arange(min_radius, int(self.radius + jump), jump):
            points += get_bounding_circle(self.center, r, r*2)
        # points += [Coordinate(0, -6) + self.center, Coordinate(2, -5) + self.center, Coordinate(4, -3) + self.center,
        #            Coordinate(6, 0)+self.center]
        print("radius", self.radius)
        print("center",self.center)
        print("points",[Coordinate(0, -6) + self.center, Coordinate(2, -5) + self.center, Coordinate(4, -3) + self.center,
                   Coordinate(6, 0)+self.center])
        return points
