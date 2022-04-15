import pygame
import sys


class Keylog:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((100,100))
        pygame.display.set_caption('Key recording device')

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    print(event.key)

            self.screen.fill((1, 1, 1))
            pygame.display.flip()


if __name__ == '__main__':
    a = Keylog()
    a.run()