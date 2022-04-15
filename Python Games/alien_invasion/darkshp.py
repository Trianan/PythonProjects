import pygame


class DarkShip:
    def __init__(self, blue_inst):
        self.screen = blue_inst.screen
        self.screen_rect = blue_inst.screen.get_rect()

        self.image = pygame.image.load('images/dark_ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        # Movement Flags:
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        # Vertical Movement:
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
        # Horizontal Movement:
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
