import pygame
from classes.pieces.Piece import Piece
from constants.constants import COLUMNS, ROWS

class Knight(Piece):
    def __init__(self, row: int, col: int, isWhite: bool):
        super().__init__(row, col, isWhite)

        imgPath: str = "assets/" + self.colour + "/knight.png"
        self.pieceImg = pygame.image.load(imgPath).convert_alpha()

    def calcAvailableMoves(self, board: list[list[int | Piece]]) -> set((int,int)):
        availableMoves = set()
        for i in range(2):
            for twoSquares in (2, -2):
                for oneSquare in (1, -1):
                    x: int = self.row + (twoSquares if not i else oneSquare)
                    y: int = self.col + (oneSquare if not i else twoSquares)
                    if -1 < x < ROWS and -1 < y < COLUMNS and (board[x][y] == -1 or board[x][y].isWhite != self.isWhite):
                        print(str(self.row)+":", x, str(self.col)+":",y)
                        availableMoves.add((x,y))
        return availableMoves
    
    def movePiece(self, x: int, y: int, board: list[list[int | Piece]]) -> bool:
        moves = self.calcAvailableMoves(board)
        if (x,y) not in moves:
            return False
        board[self.row][self.col] = -1
        board[x][y] = self
        self.row = x
        self.col = y
        return True