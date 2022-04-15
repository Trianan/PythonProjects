class GameStats:

    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()

        self.game_active = False

        with open('text_files/high_score.txt') as f:
            hs = f.read()
        self.highscore = int(hs)

    def reset_stats(self):
        self.hp_remaining = self.settings.ship_hitpoints
        self.aliens_killed = 0
        self.level = 1
        self.new_high_score = 0



