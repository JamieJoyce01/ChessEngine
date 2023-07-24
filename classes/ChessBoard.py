import pygame
from classes.pieces.Bishop import Bishop
from classes.pieces.King import King
from classes.pieces.Knight import Knight
from classes.pieces.Pawn import Pawn
from classes.pieces.Queen import Queen
from classes.pieces.Rook import Rook

from constants.constants import DARK_SQUARE_COLOUR, LIGHT_SQUARE_COLOUR, SQUARE_SIZE, ROWS, COLUMNS

class ChessBoard:
    def __init__(self):
        self.board = []
    
    def drawBoard(self, win) -> None:
        win.fill(DARK_SQUARE_COLOUR)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, 
                                 LIGHT_SQUARE_COLOUR,
                                 (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                                 )

    def drawPieces(self, win) -> None:
        for row in self.board:
            for piece in row:
                if piece != -1:
                    piece.drawPiece(win)

    def populateBoard(self) -> None:
        for row in range(ROWS):
            currentRow = []
            if row == 0:
                self.fillBackRank(row, currentRow, isWhite=False)
            elif row == 1:
                self.fillPawns(row, currentRow, isWhite=False, isTravelingUpwards=False)
            elif row == ROWS-2:
                self.fillPawns(row, currentRow, isWhite=True, isTravelingUpwards=True)
            elif row == ROWS-1:
                self.fillBackRank(row, currentRow, isWhite=True)
            else:
                for _ in range(COLUMNS):
                    currentRow.append(-1)
            self.board.append(currentRow)

    def fillBackRank(self, rowNumber: int, row: list, isWhite: bool) -> None:
        row.append(Rook(rowNumber, 0, isWhite))
        row.append(Knight(rowNumber, 1, isWhite))
        row.append(Bishop(rowNumber, 2, isWhite))
        row.append(Queen(rowNumber, 3, isWhite))
        row.append(King(rowNumber, 4, isWhite))
        row.append(Bishop(rowNumber, 5, isWhite))
        row.append(Knight(rowNumber, 6, isWhite))
        row.append(Rook(rowNumber, 7, isWhite))

    def fillPawns(self, rowNumber: int, row: list, isWhite: bool, isTravelingUpwards: bool) -> None:
        for i in range(COLUMNS):
            row.append(Pawn(rowNumber, i, isWhite, isTravelingUpwards))

                