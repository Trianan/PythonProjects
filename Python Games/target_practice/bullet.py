import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, game):

        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.colour = self.settings.bullet_colour
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):

        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)
