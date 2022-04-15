import pygame


class Ship:

    def __init__(self, game):

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load("images/target_ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def blit_ship(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
