import pygame
from classes.pieces.Piece import Piece
from constants.constants import COLUMNS

class Pawn(Piece):
    def __init__(self, row: int, col: int, isWhite: bool, isTravelingUpwards: bool):
        super().__init__(row, col, isWhite)
        self.isTravelingUpwards = isTravelingUpwards
        self.firstMove = True
        self.moveDistance = 2 if self.firstMove else 1 
        imgPath = "assets/" + self.colour + "/pawn.png"
        self.pieceImg = pygame.image.load(imgPath).convert_alpha()
        
        if not self.isWhite:
            self.moveDistance * -1
    
    def calcAvailableMoves(self, board) -> set((int,int)):
        # Since the calculation happens after we select where we are moving, we cant select off the board
        # so we done have any vertical out of index errors, we only need to cover the diagonal tiles.
        availableMoves = set()
        directionModifier = 1 if self.isTravelingUpwards else -1
        one: int = -1*directionModifier
        two: int = -2*directionModifier
        print(one,two)
        if board[self.row+one][self.col] == -1:
            availableMoves.add((self.row+one, self.col))
        if self.firstMove and board[self.row+two][self.col] == -1:
            availableMoves.add((self.row+two, self.col))
        if self.col+1 < COLUMNS and board[self.row+one][self.col+1] != -1:
            availableMoves.add((self.row+one, self.col+1))
        if self.col-1 > 0 and board[self.row+one][self.col-1] != -1:
            availableMoves.add((self.row+one, self.col-1))

        return availableMoves

    
    def movePiece(self, x: int, y: int, board: list[list[int | Piece]]) -> bool:
        # check that x,y does not exceed board
        if (x,y) not in self.calcAvailableMoves(board):
            return False
        board[self.row][self.col] = -1
        board[x][y] = self
        self.row = x
        self.col = y
        self.firstMove = False
        return True
