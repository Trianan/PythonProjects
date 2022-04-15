import pygame
from pygame.sprite import Sprite

from platform_object import Platform


class Levels:
    """Generates each level's platforms and other assets."""
    def __init__(self, platform_game):
        """Initializes attributes needed for all levels."""
        self.game_instance = platform_game
        self.settings = platform_game.settings
        self.screen = platform_game.screen
        self.screen_rect = self.screen.get_rect()

    def level_01(self):
        """Initializes Level 1."""
        level_01_platforms = pygame.sprite.Group()
        base_platform = Platform(self.game_instance, self.screen_rect.width, 40, self.settings.platform_colour,
                                 0, (self.screen_rect.height - 40), speed=0)
        platform_01 = Platform(self.game_instance, 100, 40, self.settings.platform_colour, 250, 700, speed=0.1)
        platform_02 = Platform(self.game_instance, 80, 40, self.settings.platform_colour, 10, 600, speed=0.3)
        level_01_platforms.add(platform_01, platform_02, base_platform)

        return level_01_platforms
