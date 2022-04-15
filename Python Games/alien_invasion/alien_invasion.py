import sys
from time import sleep
from pygame import mixer

import pygame

from settings import Settings
from button import Button
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from scoreboard import Scoreboard


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game and create game resources."""
        # 1: This method initializes the background settings needed for Pygame to work properly.
        pygame.init()
        # 10: Imported Settings() from settings module:
        self.settings = Settings()

        # 2: This creates a display window for the graphical elements of the game. The tuple inside the arguments
        # for set_mode() defines the dimensions of the game window. This is then assigned to "self.screen" so it
        # is available in all methods contained in this class. This object assigned to "self.screen" is called
        # a surface, which is the part of the screen where game elements can be displayed, which are their
        # surfaces themselves. The surface is redrawn on every pass through the animation loop of the game.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion!")

        # Create an instance to store game statistics, and a scoreboard to display them.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # This creates an instance of ship with the argument "self", which gives the ship class access to the game's
        # resources such as the "screen" object.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make play button:
        self.play_button = Button(self, "Play")

        self._initialize_difficulty_buttons()

    def run_game(self):
        """Start the main loop for the game."""
        # 3: The game is controlled by the run_game() method, which contains a continuously-running while-loop; this
        # contains an event loop that listens to and responds appropriately to actions the user takes while playing
        # the game, like pressing a key or moving the mouse.
        # This while-loop also contains code for managing screen updates.
        while True:
            # Calls helper methods from within class; this simplifies the main game loop.
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _initialize_difficulty_buttons(self):
        """Initializes a set of buttons for selecting difficulty, and/or resets them to default state."""
        # Difficulty buttons (Needs refactoring):
        self.normal_button = Button(self, "Normal", button_colour=(0, 0, 255))
        self.normal_button.rect.top = self.play_button.rect.bottom
        self.normal_button.msg_image_rect.center = self.normal_button.rect.center

        self.easy_button = Button(self, "Easy", button_colour=(0, 255, 0))
        self.easy_button.rect.topright = self.normal_button.rect.topleft
        self.easy_button.msg_image_rect.center = self.easy_button.rect.center

        self.hard_button = Button(self, "Hard", button_colour=(255, 0, 0))
        self.hard_button.rect.topleft = self.normal_button.rect.topright
        self.hard_button.msg_image_rect.center = self.hard_button.rect.center

    def _check_events(self):
        """Respond to key presses and mouse events."""
        # 4: Event loop that watches for keyboard and mouse events. To access these events, we'll use the
        # pygame.event.get() function, which returns a list of events that have taken place since the last time
        # the function was called. Any keyboard or mouse event will cause this for-loop to execute, which contains
        # various if-statements to respond to different events caused by user-input.
        for event in pygame.event.get():
            # 5: If the game detects a pygame.QUIT event when the player clicks the window's close button, the game
            #  will exit by calling sys.exit()
            if event.type == pygame.QUIT:
                with open("text_files/high_score.txt", 'w') as f:
                    f.write(self.stats.high_score)
                sys.exit()
            # Key presses are registered as KEYDOWN events:
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                # This registers key releases as KEYUP events.
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)

    def _check_keydown_events(self, event):
        """Responds to key-presses."""
        # This raises the ship's movement flag which increments it's position by 1 pixel to the right per loop,
        # which is done through the update() method in the ship's module.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Exit hot-key:
        if event.key == pygame.K_q:
            with open("text_files/high_score.txt", 'w') as f:
                f.write(str(self.stats.high_score))
            sys.exit()
        # Start/restart game:
        if event.key == pygame.K_p:
            self._start_game()
        # Fire bullets hot-key:
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responds to key-releases."""
        # This lowers the ships movement flag which stops movement.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_buttons(self, mouse_pos):
        """Checks the play and difficulty buttons and responds appropriately."""
        # Play button:
        play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if play_button_clicked and not self.stats.game_active:
            self._start_game()
            self._initialize_difficulty_buttons()

        # Difficulty buttons (Needs refactoring):
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        if easy_button_clicked and not self.stats.game_active:
            self._initialize_difficulty_buttons()
            self.settings.initialize_easy_settings()
            self.easy_button.button_colour = (0, 200, 0)
            print(f'Easy (speed = {self.settings.alien_speed})')

        normal_button_clicked = self.normal_button.rect.collidepoint(mouse_pos)
        if normal_button_clicked and not self.stats.game_active:
            self._initialize_difficulty_buttons()
            self.settings.initialize_normal_settings()
            self.normal_button.button_colour = (0, 0, 200)
            print(f'Normal (speed = {self.settings.alien_speed})')

        hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        if hard_button_clicked and not self.stats.game_active:
            self._initialize_difficulty_buttons()
            self.settings.initialize_hard_settings()
            self.hard_button.button_colour = (200, 0, 0)
            print(f'Hard (speed = {self.settings.alien_speed})')

    def _draw_buttons(self):
        """Draws the buttons to the screen."""
        self.play_button.draw_button()
        self.normal_button.draw_button()
        self.easy_button.draw_button()
        self.hard_button.draw_button()

    def _start_game(self):
        """Starts/restarts the game."""
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_images()

        # Get rid of remaining bullets and aliens:
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship:
        self._create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Create a new bullet and add it to "bullets" group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            # Play fired laser noise:
            laser_sound = mixer.Sound("sounds/fire_laser.wav")
            laser_sound.play()

    def _update_bullets(self):
        """Updates positions of bullets and deletes off-screen ones."""
        self.bullets.update()
        # Removes off-screen bullets.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Responds to bullet alien collisions."""
        # Check for any bullets that have hit aliens, and remove the bullet and alien if collision is detected.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            # Play explosion noise:
            alien_hit_sound = mixer.Sound('sounds/alien_destroyed.wav')
            alien_hit_sound.play()

            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self._start_next_level()

    def _start_next_level(self):
        """Begins the next level after a fleet has been cleared."""
        # Play new-level noise:
        new_level_jingle = mixer.Sound('sounds/next_level.wav')
        new_level_jingle.play()

        # Destroy existing bullets and create a new fleet.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()
        # Increase level:
        self.stats.level += 1
        self.sb.prep_level()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien, and find the number of aliens in a row after calculating the spacing per alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the first row of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in a row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        # Look for alien-ship collisions:
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen:
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Play shit-hit sound:
            ship_hit_sound = mixer.Sound('sounds/ship_destroyed.wav')
            ship_hit_sound.play()
            # Decrement ships_left, and update scoreboard:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # Get rid of remaining bullets and aliens:
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship:
            self._create_fleet()
            self.ship.center_ship()
            # Pause:
            sleep(0.5)
        else:
            # Play game-over sound:
            game_over_sound = mixer.Sound('sounds/game_over.wav')
            game_over_sound.play()
            # End current game:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        """Update images on the screen, then flip to the new screen."""
        # 9: The fill() method fills this "self.screen" surface with the specified colour imported from settings.
        self.screen.fill(self.settings.bg_colour)
        # This draws the ship on top of the background.
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # Draw the score information:
        self.sb.show_score()
        # Draw the play button if the game is inactive:
        if not self.stats.game_active:
            self._draw_buttons()

        # 6: This function makes the most recently drawn screen visible, by redrawing the new screen and erasing
        # the previous screen each pass through the main while-loop; operating somewhat like a flip-book. When
        # moving game elements around, it shows the new positions while erasing the old ones, which gives the
        # illusion of movement
        pygame.display.flip()


if __name__ == '__main__':
    # 7: Makes a game instance and runs the game, if run as the main program and not as an imported class.
    ai = AlienInvasion()
    ai.run_game()

