from __future__ import annotations
import numpy as np
import os
from Pion import Pion


class Damier:
    DIMENSION: int = 10

    def __init__(self) -> None:
        self.damier: np.ndarray = np.array(
            [[Pion() for _ in range(self.DIMENSION)] for _ in range(self.DIMENSION)])

    def get_case(self, x: int, y: int) -> str:
        assert 0 <= x < self.DIMENSION, "x doit être compris entre 0 et 9"
        assert 0 <= y < self.DIMENSION, "y doit être compris entre 0 et 9"
        return self.damier[x][y]

    def __str__(self) -> str:
        display: str = ""
        for ligne in self.damier:
            for case in ligne:
                display += str(case)+" "
            display += "\n"
        return display

    def __repr__(self) -> str:
        return str(self.damier)


if __name__ == "__main__":
    # clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    damier = Damier()
    print(damier)
