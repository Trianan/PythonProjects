import pygame
from pygame.sprite import Sprite
from settings import Settings


class Platform(Sprite):
    """A class representing a physical platform."""

    def __init__(self, game_instance, length, height, colour, x, y, speed=0.5):
        """Initializes platform attributes."""
        super().__init__()
        self.game = game_instance
        self.settings = Settings()
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()

        # Physical attributes:
        self.length, self.height, self.colour = length, height, colour
        self.rect = pygame.Rect(0, 0, self.length, self.height)
        self.platform_direction = 1
        self.speed = speed

        # Position:
        self.rect.x, self.rect.y = x, y
        self.x, self.y = float(self.rect.x), float(self.rect.y)

    def draw_platform(self):
        """Draws platform at specified position."""
        self.screen.fill(self.colour, self.rect)

    def update_platform(self):
        """Updates the position of the platform."""
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            self.platform_direction *= -1
            self.x += self.speed * self.platform_direction
        else:
            self.x += self.speed * self.platform_direction
        self.rect.x = self.x
