import math
from typing import List

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

    def get_points(self) -> List[Coordinate]:
        angles = [math.radians(theta) for theta in range(0, 360, 40)]
        return [Coordinate(self.center.x + self.radius*math.cos(theta), self.center.y + self.radius*math.sin(theta)) for theta in angles]
