import pygame
import sys

from settings import Settings
from roboy import Roboy


class RoboyGame:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("R O B O Y !   -Version 0.01 Beta")
        self.roboy = Roboy(self)

    def run_game(self):
        while True:

            self._check_events()
            self.roboy.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_d:
            self.roboy.moving_right = True
        if event.key == pygame.K_a:
            self.roboy.moving_left = True
        if event.key == pygame.K_w:
            self.roboy.moving_up = True
        if event.key == pygame.K_s:
            self.roboy.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.roboy.moving_right = False
        if event.key == pygame.K_a:
            self.roboy.moving_left = False
        if event.key == pygame.K_w:
            self.roboy.moving_up = False
        if event.key == pygame.K_s:
            self.roboy.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.background_colour)
        self.roboy.draw_roboy()

        pygame.display.flip()


if __name__ == '__main__':
    game_instance = RoboyGame()
    game_instance.run_game()