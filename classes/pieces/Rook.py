import pygame
from classes.pieces.Piece import Piece

class Rook(Piece):
    def __init__(self, row: int, col: int, isWhite: bool):
        super().__init__(row, col, isWhite)
        self.firstMove = True

        imgPath = "assets/" + self.colour + "/rook.png"
        self.pieceImg = pygame.image.load(imgPath).convert_alpha()