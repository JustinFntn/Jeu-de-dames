from dames.core.piece import Piece, Color, PieceType
import numpy as np

class Board:
    
    SIZE = 10
    
    def __init__(self):
        self.black_pieces = []
        self.white_pieces = []
        self.init_damier()
    
    def init_damier(self)-> None:
        for i in range(0,10):
            for j in range(0,4,2):
                if i%2 == 0:
                    self.black_pieces.append(Piece(Color("black"),position=(i,j)))
                    self.white_pieces.append(Piece(Color("white"),position=(i,j+6)))
                else:
                    self.black_pieces.append(Piece(Color("black"),position=(i,j+1)))
                    self.white_pieces.append(Piece(Color("white"),position=(i,j+7)))
                
                
                
    
    def __repr__(self) -> str:
        res = "black pieces: \n"
        for piece in self.black_pieces:
            res += repr(piece) + "\n"
        res += "white pieces: \n"
        for piece in self.white_pieces:
            res += repr(piece) + "\n"
        return res

    def __str__(self) -> str:
        plateau = np.full((12,12), "  ")
        plateau[0,:] = "#"
        plateau[11,1:11] = "#"
        plateau[1:11,0] = "##"
        plateau[1:11,11] = "##"
        
        for piece in self.black_pieces + self.white_pieces:
            plateau[piece.position[0] + 1][piece.position[1] + 1] = "b " if piece.color == Color("black") else "w "
        
        for i in range(1,11):
            plateau[10][i] = plateau[10][i][0]
        
        res=""
        for i in range(0,12):
            for j in range(0,12):
                res += plateau[j][i]
            res += "\n"
        return res
             