import pygame
from classes.pieces.Piece import Piece

class Knight(Piece):
    def __init__(self, row: int, col: int, isWhite: bool):
        super().__init__(row, col, isWhite)

        imgPath = "assets/" + self.colour + "/knight.png"
        self.pieceImg = pygame.image.load(imgPath).convert_alpha()