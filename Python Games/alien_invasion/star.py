import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star."""

    def __init__(self, stars_instance):
        super().__init__()
        self.screen = stars_instance.screen

        self.image = pygame.image.load("images/star2.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
