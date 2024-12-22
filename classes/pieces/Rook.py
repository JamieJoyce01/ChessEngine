import pygame
from classes.pieces.Piece import Piece
from constants.constants import COLUMNS, ROWS


# CALC MOVES IS COOKED
class Rook(Piece):
    def __init__(self, row: int, col: int, isWhite: bool):
        super().__init__(row, col, isWhite)
        self.firstMove = True

        imgPath = "assets/" + self.colour + "/rook.png"
        self.pieceImg = pygame.image.load(imgPath).convert_alpha()

    def calcAvailableMoves(self, board: list[list[int | Piece]]) -> set[int,int]:
        availableMoves = set()

        for i in range(self.row+1, ROWS):
            if(board[i][self.col] == -1):
                availableMoves.add((i, self.col))
            elif(board[i][self.col].isWhite != self.isWhite):
                availableMoves.add((i, self.col))
                break
            else:
                # If piece is obstructing break loop
                break
        # check backwards
        for i in range(self.row-1, -1, -1):
            if(board[i][self.col] == -1):
                availableMoves.add((i, self.col))
            elif(board[i][self.col].isWhite != self.isWhite):
                availableMoves.add((i, self.col))
                break
            else:
                # If piece is obstructing break loop
                break

        # COLUMNS
        for i in range(self.col+1, COLUMNS):
            if(board[self.row][i] == -1):
                availableMoves.add((self.row, i))
            elif(board[self.row][i].isWhite != self.isWhite):
                availableMoves.add((self.row, i))
                break
            else:
                # If piece is obstructing break loop
                break

        # check backwards
        for i in range(self.col-1, -1, -1):
            if(board[self.row][i] == -1):
                availableMoves.add((self.row, i))
            elif(board[self.row][i].isWhite != self.isWhite):
                availableMoves.add((self.row, i))
                break
            else:
                # If piece is obstructing break loop
                break
            
        return availableMoves