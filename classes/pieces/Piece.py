from constants.constants import SQUARE_SIZE

class Piece:
    def __init__(self, row, col, isWhite):
        self.row = row
        self.col = col
        self.isWhite = isWhite
        self.colour = "whitePieces" if self.isWhite == True else "blackPieces"

    def calcSquareCoords(self, row: int, col: int) -> tuple:
        x: int = SQUARE_SIZE * col
        y: int = SQUARE_SIZE * row
        return (x, y)

    def drawPiece(self, win) -> None:
        win.blit(self.pieceImg, self.calcSquareCoords(self.row, self.col))

    def movePiece(self, x: int, y: int, board: list[list[int | object]]) -> bool:
        # check that x,y does not exceed board
        if (x,y) not in self.calcAvailableMoves(board):
            return False
        # if(type(board[x][y])):
        #     return False
        board[self.row][self.col] = -1
        board[x][y] = self
        self.row = x
        self.col = y
        self.firstMove = False
        return True

    