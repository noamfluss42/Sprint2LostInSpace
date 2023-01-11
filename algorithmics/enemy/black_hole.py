import math
from typing import List

import numpy as np

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate


class BlackHole(Enemy):

    def __init__(self, center: Coordinate, radius: float):
        """Initializes a new black hole object anchored at the given point

        :param center: the location of the black hole
        :param radius: radius of the post
        """
        self.center = center
        self.radius = radius

    def get_points(self, n=30) -> List[Coordinate]:
        dif = 360/n
        angles = [math.radians(theta) for theta in np.arange(0, 360, dif)]
        rad_with_dif = self.radius / (math.cos(math.radians(dif)))
        print("rad_with_dif", rad_with_dif)
        return [Coordinate(self.center.x + rad_with_dif * math.cos(theta),
                           self.center.y + rad_with_dif * math.sin(theta)) for
                theta in angles]
