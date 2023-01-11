from abc import ABC
from typing import List

from algorithmics.utils.coordinate import Coordinate


class Enemy(ABC):
    pass

    def get_points(self) -> List[Coordinate]:
        return list()