import pygame


class SidewaysShip:

    def __init__(self, s_game):
        self.screen = s_game.screen
        self.screen_rect = s_game.screen.get_rect()

        self.image = pygame.image.load("images/sideship.bmp")
        self.rect = self.image.get_rect()
        self.rect.left = self.screen_rect.left

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def blitme(self):
            self.screen.blit(self.image, self.rect)