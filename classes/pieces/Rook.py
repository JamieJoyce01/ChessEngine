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

    def calcAvailableMoves(self, board: list[list[int | Piece]]) -> set((int,int)):
        availableMoves = set()

        for i in range(self.row+1, ROWS):
            if(board[self.col][i].isWhite != self.isWhite):
                availableMoves.add((self.col, i))
                break
            if(board[self.col][i] != -1):
                # If piece is obstructing break loop
                break
            availableMoves.add((self.col, i))
        # check backwards
        for i in range(self.row-1, -1, -1):
            if(board[self.col][i].isWhite != self.isWhite):
                availableMoves.add((self.col, i))
                break
            if(board[self.col][i] != -1):
                # If piece is obstructing break loop
                break
            availableMoves.add((self.col, i ))


        # COLUMNS
        for i in range(self.col+1, COLUMNS):

            print("up column", i, self.row, board[i][self.row])
            if(board[i][self.row] != -1 and board[i][self.row].isWhite != self.isWhite):
                availableMoves.add((i, self.row))
                break
            if(board[i][self.row] != -1):
                # If piece is obstructing break loop
                break
            availableMoves.add((i, self.row))
        # check backwards
        for i in range(self.col-1, -1, -1):

            print("vr", i, self.row, board[self.col][i])
            if(board[i][self.row].isWhite != self.isWhite):
                availableMoves.add((i, self.row))
                break
            if(board[i][self.row] != -1):
                # If piece is obstructing break loop
                break
            availableMoves.add((i, self.row))
        
        print(availableMoves)
        return availableMoves
    
    def movePiece(self, x: int, y: int, board: list[list[int | Piece]]) -> bool:
        # check that x,y does not exceed board
        if (x,y) not in self.calcAvailableMoves(board):
            return False
        board[self.col][self.row] = -1
        board[x][y] = self
        self.row = y
        self.col = x
        self.firstMove = False
        return True