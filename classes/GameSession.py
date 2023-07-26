import pygame
from classes.ChessBoard import ChessBoard
from classes.pieces.Piece import Piece
from constants.constants import WIDTH, HEIGHT, FPS, SQUARE_SIZE

class GameSession:

    def gameLoop(self) -> None:
        run: bool = True
        clock = pygame.time.Clock()
        chessBoard: ChessBoard = ChessBoard()
        chessBoard.populateBoard()
        currentPiece: None | Piece = None
        whitesTurn: bool = True

        while(run):
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    y,x = pygame.mouse.get_pos()
                    x = x // SQUARE_SIZE
                    y = y // SQUARE_SIZE
                    selectedPiece: int | Piece = chessBoard.board[x][y]
                    if currentPiece == None and selectedPiece != -1 and selectedPiece.isWhite == whitesTurn:
                        currentPiece = selectedPiece
                    elif currentPiece != None:
                        if currentPiece.movePiece(x, y, chessBoard.board):
                            whitesTurn = not whitesTurn
                        currentPiece = None
            
            chessBoard.drawBoard(self.window)
            chessBoard.drawPieces(self.window)
            pygame.display.update()

    @staticmethod
    def createGameSessionFactory() -> None:
        instance = GameSession()
        instance.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")
        return instance