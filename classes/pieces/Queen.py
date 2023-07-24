import pygame
from classes.pieces.Piece import Piece

class Queen(Piece):
    def __init__(self, row: int, col: int, isWhite: bool):
        super().__init__(row, col, isWhite)

        imgPath = "assets/" + self.colour + "/queen.png"
        self.pieceImg = pygame.image.load(imgPath).convert_alpha()