import pygame
from classes.pieces.Piece import Piece
from constants.constants import COLUMNS, ROWS

class King(Piece):
    def __init__(self, row: int, col: int, isWhite: bool):
        super().__init__(row, col, isWhite)
        self.firstMove = True
        self.moveDistance = 1

        imgPath = "assets/" + self.colour + "/king.png"
        self.pieceImg = pygame.image.load(imgPath).convert_alpha()
    
    def calcAvailableMoves(self, board: list[list[int | Piece]]) -> set[int,int]:
        availableMoves = set()
        for y in [+1, 0, -1]:
            for x in [-1, 0 +1]:
                newX = self.row + x
                newY = self.col + y
                print(self.row, self.col, x, y)
                if(newX < 0 or newY < 0 or newX >= ROWS or newY >= COLUMNS):
                    continue
                elif(y == 0 and x == 0):
                    continue
                elif(board[newX][newY] == -1):
                    availableMoves.add((newX, newY))
                elif(board[newX][newY].isWhite != self.isWhite):
                    availableMoves.add((newX, newY))
        return availableMoves