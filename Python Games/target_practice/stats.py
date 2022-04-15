class Stats:

    def __init__(self, game):

        self.settings = game.settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):

        self.misses_left = self.settings.target_misses_allowed
        self.hits = 0

