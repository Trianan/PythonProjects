import pygame
from pygame.sprite import Sprite


class Droplet(Sprite):
    def __init__(self, raindrops_instance):
        super().__init__()
        self.screen = raindrops_instance.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/raindrop.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.bottom = self.screen_rect.top

    def update(self):
        self.rect.bottom += 1

    def check_edges(self):
        if self.rect.top >= self.screen_rect.bottom:
            return True
