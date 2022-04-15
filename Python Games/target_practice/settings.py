class Settings:

    def __init__(self):

        # Screen settings:
        self.screen_width = 1000
        self.screen_height = 800
        self.background_colour = (27, 28, 51)

        # Target settings:
        self.target_misses_allowed = 3

        # Bullet settings:
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_colour = (255, 0, 0)
        self.bullet_limit = 5

        # Difficulty scaling factor:
        self.speedup_factor = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        self.target_direction = 1
        self.target_speed = 0.5

        self.bullet_speed = 1.0
        self.ship_speed = 1.0

    def speedup_game(self):

        self.ship_speed *= self.speedup_factor
        self.bullet_speed *= self.speedup_factor
        self.target_speed *= self.speedup_factor

