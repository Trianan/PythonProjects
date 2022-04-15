import pygame
import sys
from darkshp import DarkShip


class BlueScreen:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Blue Screen')
        self.bg_colour = (0, 0, 200)
        self.shp = DarkShip(self)

    def run_blue(self):
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        self.shp.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.shp.moving_down = True
                    if event.key == pygame.K_LEFT:
                        self.shp.moving_left = True
                    if event.key == pygame.K_RIGHT:
                        self.shp.moving_right = True

                elif event.type == pygame.KEYUP:

                    if event.key == pygame.K_UP:
                        self.shp.moving_up = False
                    if event.key == pygame.K_DOWN:
                        self.shp.moving_down = False
                    if event.key == pygame.K_LEFT:
                        self.shp.moving_left = False
                    if event.key == pygame.K_RIGHT:
                        self.shp.moving_right = False



            self.screen.fill(self.bg_colour)
            self.shp.update()
            self.shp.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    bs = BlueScreen()
    bs.run_blue()

