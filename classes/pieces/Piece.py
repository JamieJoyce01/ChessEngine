from constants.constants import SQUARE_SIZE

class Piece:
    def __init__(self, row, col, isWhite):
        self.row = row
        self.col = col
        self.isWhite = isWhite
        self.colour = "whitePieces" if self.isWhite == True else "blackPieces"

    def drawPiece(self, win) -> None:
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row

        win.blit(self.pieceImg, (self.x, self.y))