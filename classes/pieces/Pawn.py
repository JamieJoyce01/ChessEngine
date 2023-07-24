import pygame
from classes.pieces.Piece import Piece

class Pawn(Piece):
    def __init__(self, row: int, col: int, isWhite: bool):
        super().__init__(row, col, isWhite)
        self.firstMove = True
        self.moveDistance = 2 if self.firstMove else 1 
        imgPath = "assets/" + self.colour + "/pawn.png"
        self.pieceImg = pygame.image.load(imgPath).convert_alpha()
        
        if not self.isWhite:
            self.moveDistance * -1