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
