import pygame
from pygame.sprite import Sprite


class Target(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load("images/target.bmp")
        self.rect = self.image.get_rect()

        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)

    def check_edges(self):
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            self.settings.target_direction *= -1

    def update(self):
        self.y += (self.settings.target_speed * self.settings.target_direction)
        self.rect.y = self.y

    def center_target(self):
        self.rect.midright = self.screen_rect.midright

    def draw_target(self):
        self.screen.blit(self.image, self.rect)



