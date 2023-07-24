import pygame
from classes.pieces.Piece import Piece

class Bishop(Piece):
    def __init__(self, row: int, col: int, isWhite: bool):
        super().__init__(row, col, isWhite)

        imgPath = "assets/" + self.colour + "/bishop.png"
        self.pieceImg = pygame.image.load(imgPath).convert_alpha()