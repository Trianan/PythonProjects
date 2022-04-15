import pygame
import sys

from pygame.sprite import Sprite
from droplet import Droplet


class Raindrops:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((595, 528))
        self.screen_rect = self.screen.get_rect()
        self.screen_width, self.screen_height = self.screen_rect.size
        pygame.display.set_caption("It's Raining!")
        self.raindrops = pygame.sprite.Group()

        self._create_rainstorm()

    def start_raining(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_raindrops()
            self._update_screen()

    def _create_rainstorm(self, single_row=False):
        raindrop = Droplet(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.screen_width - raindrop_width
        number_in_row = available_space_x // (2 * raindrop_width)

        available_space_y = self.screen_height
        number_of_rows = available_space_y // (2 * raindrop_height)
        if single_row:
            number_of_rows = 1

        for row in range(number_of_rows):
            for drops in range(number_in_row):
                self._create_raindrop(drops, row)

    def _check_rainstorm_edges(self):
        for raindrop in self.raindrops.sprites():
            if raindrop.rect.top >= self.screen_rect.bottom:
                raindrop.rect.bottom = self.screen_rect.top

    def _create_raindrop(self, drops, row):
        raindrop = Droplet(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.rect.x = raindrop_width + (2 * raindrop_width) * drops
        raindrop.rect.bottom = self.screen_rect.top + (2 * raindrop_height) * row
        self.raindrops.add(raindrop)

    def _update_raindrops(self):
        self.raindrops.update()
        self._check_rainstorm_edges()
        print(len(self.raindrops))

    def _update_screen(self):
        self.screen.fill((34, 32, 52))
        self.raindrops.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    rd = Raindrops()
    rd.start_raining()
