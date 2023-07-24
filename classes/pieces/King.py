import pygame
from classes.pieces.Piece import Piece

class King(Piece):
    def __init__(self, row: int, col: int, isWhite: bool):
        super().__init__(row, col, isWhite)
        self.firstMove = True
        self.moveDistance = 1

        imgPath = "assets/" + self.colour + "/king.png"
        self.pieceImg = pygame.image.load(imgPath).convert_alpha()