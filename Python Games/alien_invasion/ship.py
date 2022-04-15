import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        super().__init__()
        """Initialize the ship and set its starting position."""
        # This assigns the screen as an attribute of Ship so it's accessible to the rest of the methods in this class.
        # It also contains a reference to the current instance of the game (ai_game).
        self.screen = ai_game.screen
        # Import game settings to use in methods in this class.
        self.settings = ai_game.settings
        # This accesses the screens "rect" attribute using the get_rect() method, which allows to access it and use it
        # to draw the ship at the correct position on the screen.
        self.screen_rect = ai_game.screen.get_rect()

        # This loads the image and returns it as a surface representing the ship; it then assigns it to an attribute,
        # which is then used to access the ship surface's rect attribute to place it correctly on screen.
        self.image = pygame.image.load('images/ship_plain.bmp')
        self.rect = self.image.get_rect()

        # This positions the ship at the bottom center of the screen; it does this by matching the ship's position to
        # the "midbottom" location of the screen's rect, centering it on the bottom edge of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags:
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship location based on it's movement flags."""
        # Updates x-value and not actual rect location.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

