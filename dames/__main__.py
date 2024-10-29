from dames.core.board import Board
from dames.core.piece import Piece, Color, PieceType 

if __name__=="__main__":
    b:Piece = Piece(Color("black"))
    print(repr(b))
    b.position = (1,1)
    print(repr(b))