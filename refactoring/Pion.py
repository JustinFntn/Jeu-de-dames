from __future__ import annotations
from abc import ABC, abstractmethod


class Pion(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def default(self) -> None:
        print("default")


if __name__ == "__main__":
    pion = Pion()
    pion.default()
