class Settings:
    """A class to store the settings of the platformer game."""
    def __init__(self):
        # Screen settings:
        self.screen_dimensions = (1000, 800)
        # Colours:
        self.background_colour = (150, 25, 150)

        # Platform settings:
        self.platform_colour = (50, 50, 50)
        # Player settings:
        self.player_delta_x = 0
        self.player_horizontal_acceleration = 0
        self.player_deceleration = 0.99
        self.player_max_speed = 4

        self.jump_velocity = 0
        self.player_gravity = 0.005





