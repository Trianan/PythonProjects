import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load("images/alien2.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_rect.right
        self.rect.y = self.screen_rect.top

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.alien_speed
        self.rect.x = self.x

