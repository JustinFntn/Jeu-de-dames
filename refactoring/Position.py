from __future__ import annotations


class Position:

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x: int = x
        self.y: int = y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def set_x(self, x: int) -> None:
        self.x = x

    def set_y(self, y: int) -> None:
        self.y = y

    def __sub__(self, other: Position) -> Position:
        return Position(self.x - other.x, self.y - other.y)

    def __add__(self, other: Position) -> Position:
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other: Position) -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"Position: x={self.x}, y={self.y}"

    def __repr__(self) -> str:
        return f"Position({self.x}, {self.y})"


if __name__ == "__main__":
    pos1: Position = Position(3, 4)
    pos2: Position = Position(3, 4)
    print(pos1-pos2)
