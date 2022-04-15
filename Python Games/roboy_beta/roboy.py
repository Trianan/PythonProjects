import pygame


class Roboy:

    def __init__(self, game):

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('images/roboy.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags:
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.roboy_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.roboy_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.roboy_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.roboy_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw_roboy(self):
        self.screen.blit(self.image, self.rect)


