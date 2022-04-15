import pygame
from pygame.sprite import Sprite


class Dude:
    """A class to represent the player character."""
    def __init__(self, game_instance, x=0, y=0):
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game_instance.settings

        self.image = pygame.image.load('images/platformer_dude.png')
        self.rect = self.image.get_rect()

        # Position and orientation:
        self.direction = 'right'
        self.rect.x, self.rect.y = x, y
        self.x, self.y = float(self.rect.x), float(self.rect.y)
        # Movement flags:
        self.is_stationary = True
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.falling = False

    def update_dude(self):

        # HORIZONTAL MOVEMENT W. ACCELERATION

        # Flags indicating if player is in motion:
        if self.moving_right ^ self.moving_left:
            self.is_stationary = False
        else:
            self.is_stationary = True

        # Horizontal Movement & Direction:
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.direction = 'right'
            self.x += self.settings.player_speed

        if self.moving_left and self.rect.left > 0:
            self.direction = 'left'
            self.x -= self.settings.player_speed

        # Acceleration (This "^" is a XOR, needed to prevent acceleration stacking.):
        if self.moving_right ^ self.moving_left:
            self.settings.player_speed += self.settings.player_horizontal_acceleration

        # This resets the player's speed when movement stops:
        if self.is_stationary:
            self.settings.player_speed = 1.0

        self.rect.x = self.x

    def blit_dude(self):
        if self.direction == 'right':
            self.screen.blit(self.image, self.rect)
        elif self.direction == 'left':
            self.screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
