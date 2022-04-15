import pygame
import sys
from sideways_shooter_ship import SidewaysShip
from sideways_bullet import SidewaysBullet


class SidewaysShooter:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 700))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Sideways Shooter!')
        self.bg_colour = (6, 18, 6)

        self.ship = SidewaysShip(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.ship.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.ship.moving_down = True
                    if event.key == pygame.K_SPACE:
                        self._fire_bullet()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.ship.moving_up = False
                    if event.key == pygame.K_DOWN:
                        self.ship.moving_down = False

            self.ship.update()
            self._update_bullets()

            self.screen.fill(self.bg_colour)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
            # Remove when finished the program:
            print(len(self.bullets))

    def _fire_bullet(self):
        if len(self.bullets) < 5:
            new_bullet = SidewaysBullet(self)
            self.bullets.add(new_bullet)


if __name__ == '__main__':

    s_game = SidewaysShooter()
    s_game.run_game()


