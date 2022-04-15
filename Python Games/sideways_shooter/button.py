import pygame.font


class Button:

    def __init__(self, game, message, button_colour=(100, 100, 100), text_colour=(255, 255, 255)):

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_colour = button_colour
        self.text_colour = text_colour

        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_message(message)

    def prep_message(self, message):
        self.message_image = self.font.render(message, True, self.text_colour, self.button_colour)
        self.message_rect = self.message_image.get_rect()
        self.message_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.message_image, self.message_rect)


