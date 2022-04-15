import pygame
import sys
from pygame.sprite import Sprite
from star import Star
from random import randint


class DisplayStars:
    """A class to display stars on screen."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.screen_rect = self.screen.get_rect()
        self.screen_width, self.screen_height = self.screen.get_rect().size
        pygame.display.set_caption('Stars!!!')

        self.stars = pygame.sprite.Group()

        self._create_starfield()

    def run_stars(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_screen()

    def _create_starfield(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_rect.width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        available_space_y = self.screen_rect.height - (2 * star_height)
        star_rows = available_space_y // (2 * star_height)

        for star_row in range(star_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, star_row)

    def _create_star(self, star_number, star_row):
        random_number = randint(0, 800)
        star = Star(self)
        star_width, star_height = star.rect.size
        star.rect.x = star_width + 1.5 * star_number * random_number  # * star_width
        star.rect.y = star_height + 1.5 * star_row * random_number  # * star_height
        self.stars.add(star)

    def _update_screen(self):
        self.screen.fill((20, 24, 46))
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    stars = DisplayStars()
    stars.run_stars()