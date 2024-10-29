from __future__ import annotations
from enum import Enum


class Color(Enum):
    WHITE = "white"
    BLACK = "black"


class PieceType(Enum):
    PAWN = "pawn"
    QUEEN = "queen"


class Piece:
    def __init__(self, color: Color, piece_type: PieceType = PieceType.PAWN,position:tuple[int,int]=(0,0)) -> None:
        self.color: Color = color
        self.piece_type: PieceType = piece_type
        self._position:tuple[int, int] = position
        
    @property
    def position(self) -> tuple[int,int]:
        return self.position
    
    @position.setter
    def position(self, new_position: tuple[int,int]) -> None:
        self._position = new_position

    def __str__(self) -> str:
        if self.piece_type == PieceType.PAWN:
            return self.color.value[0]
        else:
            return self.color.value[0].upper()

    def __repr__(self) -> str:
        return f'{self.color}-{self.piece_type}: {self._position}'

