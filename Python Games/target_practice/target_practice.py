import pygame
import sys
from time import sleep

from settings import Settings
from ship import Ship
from target import Target
from bullet import Bullet
from stats import Stats
from button import Button


class TargetPractice:

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.ship = Ship(self)
        self.target = Target(self)
        self.stats = Stats(self)
        self.bullets = pygame.sprite.Group()
        self.play_button = Button(self, "Play game!")

    # MAIN LOOP:

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()
            self._update_screen()

    def _reset_game(self):
        self.stats.reset_stats()
        self.stats.game_active = True
        self.bullets.empty()
        self.ship.center_ship()
        self.target.center_target()
        pygame.mouse.set_visible(False)

    # CONTROLS & EVENT MANAGEMENT:

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                self._check_keydown(event)

            if event.type == pygame.KEYUP:
                self._check_keyup(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_play_button(mouse_position)

    def _check_keydown(self, event):
        # Game quit, reset, & start keys:
        if event.key == pygame.K_q:
            sys.exit()
        # Movement controls:
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        # Bullet controls:
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup(self, event):
        # Movement controls:
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_position):
        button_clicked = self.play_button.rect.collidepoint(mouse_position)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self._reset_game()

    # SPRITE & SHIP MANAGEMENT:

    def _update_target(self):
        self.target.check_edges()
        self.target.update()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_limit:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
                self.missed_target()

        collisions = pygame.sprite.spritecollide(self.target, self.bullets, True)
        if collisions:
            self.stats.hits += 1
            print(f"Target hit! {self.stats.hits}")
            if self.stats.hits == 3:
                self.settings.speedup_game()
                print(self.settings.target_speed)
                self.stats.hits = 0

    def missed_target(self):
        if self.stats.misses_left > 0:
            self.stats.misses_left -= 1
            print(f"You missed! Misses left: {self.stats.misses_left}")
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    # SCREEN METHODS:

    def _update_screen(self):
        self.screen.fill(self.settings.background_colour)
        self.ship.blit_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.draw_target()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()


if __name__ == "__main__":
    game = TargetPractice()
    game.run_game()
