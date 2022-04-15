import pygame
from pygame.sprite import Sprite


class Dude(Sprite):
    """A class to represent the player character."""
    def __init__(self, game_instance, x=0, y=0):
        super().__init__()
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game_instance.settings

        self.image = pygame.image.load('images/platformer_dude.png')
        self.rect = self.image.get_rect()

        # Position and orientation:
        self.direction = 'right'
        self.rect.x, self.rect.y = x, y
        self.x, self.y = float(self.rect.x), float(self.rect.y)
        # Horizontal movement flags:
        self.delta_x = 0
        self.is_moving_right = False
        self.is_moving_left = False
        # Vertical Movement Flags:
        self.delta_y = 0
        self.jumping = False
        self.is_falling = False
        self.on_platform = False

    def update_dude(self):

        # HORIZONTAL MOVEMENT:

        # Stops player if both horizontal-movement keys are held down:
        if self.is_moving_right and self.is_moving_left:
            self.settings.player_horizontal_acceleration = 0
        if not self.is_moving_right and not self.is_moving_left:
            self.settings.player_horizontal_acceleration = 0

        # Constraints to keep player on screen:
        if self.rect.left < 0:
            self.is_moving_left = False
            self.delta_x = 0
        if self.rect.right > self.screen_rect.right:
            self.is_moving_right = False
            self.delta_x = 0

        # Accelerates player in direction of horizontal motion:
        if self.is_moving_right ^ self.is_moving_left:
            self.delta_x += self.settings.player_horizontal_acceleration
            if abs(self.delta_x) >= self.settings.player_max_speed:
                self.delta_x = (self.delta_x/abs(self.delta_x)) * self.settings.player_max_speed

        # Decelerates if player releases keys or has both horizontal keys held down:
        if self.settings.player_horizontal_acceleration == 0:
            self.delta_x *= self.settings.player_deceleration

        # Changes x-position of player, and converts it from a floating value into an integer.
        self.x += self.delta_x
        self.rect.x = self.x

        # VERTICAL MOVEMENT:

        # Gravity:
        if self.jumping and self.on_platform:
            self.delta_y += self.settings.jump_velocity
            self.on_platform = False

        if not self.on_platform:
            self.delta_y += self.settings.player_gravity

        if self.on_platform:
            self.delta_y = 0

        self.y += self.delta_y
        self.rect.y = self.y

    def blit_dude(self):
        if self.direction == 'right':
            self.screen.blit(self.image, self.rect)
        elif self.direction == 'left':
            self.screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
