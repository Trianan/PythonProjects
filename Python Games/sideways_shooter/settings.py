class Settings:

    def __init__(self):

        # Screen settings:
        self.screen_width = 1400
        self.screen_height = 700
        self.background_colour = (0, 0, 0)

        # Ship settings:
        self.ship_speed = 1.5
        self.ship_hitpoints = 5

        # Bullet settings:
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (255, 0, 0)
        self.bullet_limit = 5

        # Alien settings:
        self.alien_speed = 0.25
        self.max_aliens = 2

        self.speedup_factor = 1.1

    def initialize_dynamic_settings(self):
        self.alien_speed = 0.30
        self.ship_speed = 1.00
        self.bullet_speed = 1.75
        self.max_aliens = 2

    def increase_difficulty(self):
        self.alien_speed *= self.speedup_factor
        self.ship_speed *= self.speedup_factor
        self.bullet_speed *= self.speedup_factor
