class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings:
        self.screen_width = 1200
        self.screen_height = 800
        # 8: This sets the RBG-specified colour, (255, 0, 0) = red, (0, 255, 0) = green, and (0, 0, 255) = blue. These
        # can be mixed with different values to create up to 16-million colours. We assign this value to self.bg_colour
        # so it can be accessed throughout the class.
        self.bg_colour = (230, 230, 230)

        # Ship settings:
        self.ship_limit = 3

        # Bullet settings:
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_colour = (255, 0, 0)
        self.bullets_allowed = 3

        # Alien settings:
        self.fleet_drop_speed = 10

        # Factor by which the game speeds up:
        self.speedup_scale = 1.1

        # Factor by which the alien point-values increase:
        self.score_scale = 1.5

        # Dynamic settings (These aren't actually used!):
        self.ship_speed = 0
        self.bullet_speed = 0
        self.alien_speed = 0
        self.alien_points = 0

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

        self.initialize_easy_settings()

    def initialize_easy_settings(self):
        """Initialize settings that change over the course of a game."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def initialize_normal_settings(self):
        self.ship_speed = 2.0
        self.bullet_speed = 2.0
        self.alien_speed = 1.5
        self.fleet_direction = 1
        self.alien_points = 60

    def initialize_hard_settings(self):
        self.ship_speed = 2.5
        self.bullet_speed = 2.5
        self.alien_speed = 2.0
        self.fleet_direction = 1
        self.alien_points = 70

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
