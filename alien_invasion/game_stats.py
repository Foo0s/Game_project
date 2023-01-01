class GameStats():
    def __init__(self, ai_sup_game):
        "Статистика..."
        self.settings = ai_sup_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        'Инициализация статистики..'
        self.ships_left = self.settings.ship_limit
        self.score = 0
