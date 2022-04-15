import pygame
import sys
from time import sleep
from random import randint
from pygame import mixer

from settings import Settings
from sideways_ship import SidewaysShip
from sideways_bullet import SidewaysBullet
from sideways_alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class SidewaysShooter:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.settings.screen_width, self.settings.screen_height = self.screen_rect.width, self.screen_rect.height
        pygame.display.set_caption('Sideways Shooter!')

        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)
        self.ship = SidewaysShip(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.play_button = Button(self, "Play!")

        self.settings.initialize_dynamic_settings()
        self._spawn_aliens()

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._spawn_aliens()

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                with open('text_files/high_score.txt', 'w') as f:
                    f.write(str(self.stats.highscore))
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
                if event.key == pygame.K_q:
                    with open('text_files/high_score.txt', 'w') as f:
                        f.write(str(self.stats.highscore))
                    sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self.check_play_button(mouse_position)

    def check_play_button(self, mouse_position):
        button_clicked = self.play_button.rect.collidepoint(mouse_position)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        self.stats.reset_stats()
        self.scoreboard.prep_images()
        self.settings.initialize_dynamic_settings()
        self.stats.game_active = True

        self.aliens.empty()
        self.bullets.empty()

        self.ship.center_ship()
        pygame.mouse.set_visible(False)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
            # Remove when finished the program:
            # print(len(self.bullets))
            self._check_collisions()

    def _check_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            alien_killed_sound = mixer.Sound('sounds/alien_destroyed.wav')
            alien_killed_sound.play()

            for alien_killed in collisions.values():
                self.stats.aliens_killed += 1 * len(alien_killed)
            self.scoreboard.prep_kills()
            self.scoreboard.check_highscore()
            self._check_stage()

    def _check_stage(self):
        if self.stats.aliens_killed % 15 == 0:
            level_up_sound = mixer.Sound('sounds/next_level.wav')
            level_up_sound.play()
            self.settings.increase_difficulty()

            self.stats.level += 1
            self.scoreboard.prep_level()

            if self.stats.level % 5 == 0:
                self.settings.max_aliens += 1

    def _ship_hit(self):
        if self.stats.hp_remaining > 0:
            ship_hit_sound = mixer.Sound('sounds/ship_destroyed.wav')
            ship_hit_sound.play()
            self.stats.hp_remaining -= 1
            self.scoreboard.prep_lives()
            sleep(0.5)
        else:
            game_over_sound = mixer.Sound('sounds/game_over.wav')
            game_over_sound.play()
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_limit:
            laser_noise = mixer.Sound("sounds/fire_laser.wav")
            laser_noise.play()
            new_bullet = SidewaysBullet(self)
            self.bullets.add(new_bullet)

    def _spawn_aliens(self):
        if len(self.aliens) < self.settings.max_aliens:
            self._create_alien()

    def _update_aliens(self):
        self.aliens.update()

        alien_crash = pygame.sprite.spritecollideany(self.ship, self.aliens)
        if alien_crash:
            self.aliens.remove(alien_crash)
            self._ship_hit()

        for alien in self.aliens.copy():
            if alien.rect.right <= 0:
                self.aliens.remove(alien)
                self._ship_hit()

    def _create_alien(self):
        alien = Alien(self)
        alien_height = alien.rect.height
        random_integer = randint(0, (self.screen_rect.height - alien_height))
        alien.x = self.screen_rect.right
        alien.rect.x = alien.x
        alien.rect.y = random_integer
        self.aliens.add(alien)

    def _update_screen(self):
        self.screen.fill(self.settings.background_colour)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()
        self.scoreboard.show_scoreboard()
        pygame.display.flip()


if __name__ == '__main__':

    s_game = SidewaysShooter()
    s_game.run_game()
