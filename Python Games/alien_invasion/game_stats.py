class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an active state
        self.game_active = False
        # High score (not to be reset!):
        with open("text_files/high_score.txt") as f:
            hs = f.read()
        self.high_score = int(hs)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

        # 0 Means a high score has not been set in the current game, 1 means a new one has.
        self.new_high_score = 0
