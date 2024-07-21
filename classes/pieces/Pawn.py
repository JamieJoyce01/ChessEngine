import pygame
from classes.pieces.Piece import Piece
from constants.constants import COLUMNS

class Pawn(Piece):
    def __init__(self, row: int, col: int, team, isTravelingUpwards: bool):
        super().__init__(row, col, team)
        self.isTravelingUpwards = isTravelingUpwards
        self.firstMove = True
        imgPath = "assets/" + self.colour + "/pawn.png"
        self.pieceImg = pygame.image.load(imgPath).convert_alpha()
    
    # Bug where I took a left piece and couldnt take the next left piece.
    def calcAvailableMoves(self, board: list[list[int | Piece]]) -> set((int,int)):
        # Since the calculation happens after we select where we are moving, we cant select off the board
        # so we don't have any vertical out of index errors, we only need to cover the diagonal tiles.
        availableMoves = set()
        directionModifier = 1 if self.isTravelingUpwards else -1
        one: int = -1*directionModifier
        two: int = -2*directionModifier
        print(one,two)
        if board[self.col+one][self.row] == -1:
            availableMoves.add((self.col+one, self.row))
        if self.firstMove and board[self.col+two][self.row] == -1:
            availableMoves.add((self.col+two, self.row))
        if self.col+1 < COLUMNS and board[self.col+one][self.row+1] != -1 and board[self.col+one][self.row+1].isWhite != self.isWhite:
            availableMoves.add((self.row+one, self.col+1))
        # What is this doing?
        if self.col-1 > 0 and board[self.col+one][self.row-1] != -1 and board[self.col+one][self.row-1].isWhite != self.isWhite:
            availableMoves.add((self.col+one, self.row-1))

        return availableMoves

    # TODO Can potentially move this to parent class
    def movePiece(self, x: int, y: int, board: list[list[int | Piece]]) -> bool:
        # check that x,y does not exceed board
        if (x,y) not in self.calcAvailableMoves(board):
            return False
        board[self.col][self.row] = -1
        board[x][y] = self
        self.row = x
        self.col = y
        self.firstMove = False
        return True
