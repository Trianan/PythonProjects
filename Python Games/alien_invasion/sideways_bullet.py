import pygame
from pygame.sprite import Sprite


class SidewaysBullet(Sprite):

    def __init__(self, s_game):
        super().__init__()
        self.screen = s_game.screen

        # Bullet settings:
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (100, 100, 100)

        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = s_game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_colour, self.rect)
