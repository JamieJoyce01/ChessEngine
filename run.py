from classes.GameSession import GameSession



gameSession: GameSession = GameSession.createGameSessionFactory()
gameSession.gameLoop()