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
        currentPiece = None

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
                    selectedPiece = chessBoard.board[x][y]
                    if currentPiece == None and selectedPiece != -1:
                        currentPiece = selectedPiece
                    elif currentPiece != None:
                        currentPiece.movePiece(x, y, chessBoard.board)
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