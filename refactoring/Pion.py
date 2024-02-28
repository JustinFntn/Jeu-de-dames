from __future__ import annotations
from abc import ABC, abstractmethod


class Pion:

    def __init__(self) -> None:
        self.state: str = "○"

    # @abstractmethod
    # def default(self) -> None:
    #     print("default")

    def __str__(self) -> str:
        return self.state

    def __repr__(self) -> str:
        return self.state


if __name__ == "__main__":
    pion = Pion()
    pion.default()
