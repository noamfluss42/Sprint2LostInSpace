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
