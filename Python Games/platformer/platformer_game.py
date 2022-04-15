import pygame
from pygame.sprite import Sprite
import sys

from settings import Settings
from platform_object import Platform
# Change 'dude_movement_rework' back to 'dude' if rework doesn't fix issues.
from dude import Dude
from levels import Levels


class PlatformerGame:
    """A class to represent the instance of the platformer game."""
    def __init__(self):
        """Initialize game attributes."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('Janky-Ass Platformer of Unrivaled Fuckwit-ism!')
        self.screen_rect = self.screen.get_rect()
        # Player initialization:
        self.player = Dude(self, self.screen_rect.centerx, self.screen_rect.centery)

        # Level attributes:
        self.levels = Levels(self)
        self.level = ''
        self.load_level()

    def run_game(self):
        while True:
            self.check_events()
            self.update_platform()
            self.player.update_dude()
            self.update_screen()
            print(self.player.delta_x)
            print(self.player.delta_y)

    def check_events(self):
        """Checks for input from the user."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self._check_key_event(event)

    def _check_key_event(self, event):
        """Responds to key events."""
        # Keydown events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

            # Horizontal Movement:
            if event.key == pygame.K_d:
                self.player.direction = 'right'
                self.player.is_moving_right = True
                self.settings.player_horizontal_acceleration = 0.02
            if event.key == pygame.K_a:
                self.player.direction = 'left'
                self.player.is_moving_left = True
                self.settings.player_horizontal_acceleration = -0.02

            # Vertical Movement:
            if event.key == pygame.K_SPACE:
                self.player.jumping = True
                self.settings.jump_velocity = -1.5

        # Keyup events:
        if event.type == pygame.KEYUP:
            # Horizontal Movement:
            if event.key in (pygame.K_d, pygame.K_a):
                if event.key == pygame.K_d:
                    self.player.is_moving_right = False
                if event.key == pygame.K_a:
                    self.player.is_moving_left = False

            # Vertical Movement:
            if event.key == pygame.K_SPACE:
                self.player.jumping = False

    def load_level(self):
        self.level = self.levels.level_01()

    def draw_platforms(self):
        for platform in self.level:
            platform.draw_platform()

    def update_platform(self):
        for platform in self.level:
            platform.update_platform()

        self._check_collisions()

    def _check_collisions(self):
        platform_hits = pygame.sprite.spritecollide(self.player, self.level, False)
        if platform_hits:
            self.player.on_platform = True
            # Player moves with moving platform:
            for platform in platform_hits:
                self.player.x += (platform.speed * platform.platform_direction)
        else:
            self.player.on_platform = False

    def update_screen(self):
        """Updates the positions of elements on the screen and draws them."""
        self.screen.fill(self.settings.background_colour)
        self.draw_platforms()
        self.player.blit_dude()
        pygame.display.flip()


if __name__ == '__main__':
    platformer = PlatformerGame()
    platformer.run_game()
