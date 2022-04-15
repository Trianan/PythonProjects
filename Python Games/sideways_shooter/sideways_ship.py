import pygame
from time import sleep


class SidewaysShip:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load("images/sideship2.bmp")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed

    def center_ship(self):
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)


