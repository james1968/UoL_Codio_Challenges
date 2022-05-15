from typing import Tuple

class Point:
    def __init__(self, X: int, Y: int):
        self._x = X
        self._y = Y

    def set_coordinates(self, X: int, Y: int) -> None:
        self._x = X
        self._y = Y

    def get_coordinates(self) -> Tuple[int, int]:
        return (self._x, self._y)

    def point_to_string(self) -> str:
        return str(self.get_coordinates())

    def _is_negative(self) -> bool:
        return self._x < 0 or self._y < 0


p = Point(45, 15)

X = p._x
p._x = 10
print(p.point_to_string())
print(p._is_negative())
p.__init__(10,20)
print(p)