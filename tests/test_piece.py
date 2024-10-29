import unittest
from dames.core.piece import Piece, Color, PieceType

class TestPiece(unittest.TestCase):
    def test_init(self):
        '''test de l'initialisation de la classe Piece
        '''        
        piece = Piece(Color.WHITE, PieceType.PAWN)
        self.assertEqual(piece.color, Color.WHITE, msg='La couleur de la pièce est incorrecte')
        self.assertEqual(piece.piece_type, PieceType.PAWN, msg='Le type de la pièce est incorrect')
        
if __name__ == "__main__":
    unittest.main()