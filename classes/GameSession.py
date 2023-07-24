import pygame
from classes.ChessBoard import ChessBoard
from constants.constants import WIDTH, HEIGHT, FPS

class GameSession:

    def gameLoop(self) -> None:
        run: bool = True
        clock = pygame.time.Clock()
        chessBoard: ChessBoard = ChessBoard()
        chessBoard.populateBoard()

        while(run):
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            
            chessBoard.drawBoard(self.window)
            chessBoard.drawPieces(self.window)
            pygame.display.update()

    @staticmethod
    def createGameSessionFactory() -> None:
        instance = GameSession()
        instance.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")
        return instance