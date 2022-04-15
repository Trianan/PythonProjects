import pygame.font
from pygame import mixer


class Scoreboard:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_colour = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_images()

    def prep_kills(self):
        kills_str = f'Kills: {self.stats.aliens_killed}'
        self.kills_image = self.font.render(kills_str, True, self.text_colour)  # ,self.settings.background_colour
        self.kills_rect = self.kills_image.get_rect()
        self.kills_rect.right = self.screen_rect.right - 10
        self.kills_rect.top = self.screen_rect.top + 10

    def prep_highscore(self):
        highscore_str = f'Highscore: {self.stats.highscore}'
        self.highscore_image = self.font.render(highscore_str, True, self.text_colour)
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.kills_rect.top

    def check_highscore(self):
        if self.stats.aliens_killed > self.stats.highscore:
            if self.stats.new_high_score < 1:
                high_score_sound = mixer.Sound('sounds/high_score.wav')
                high_score_sound.play()
                self.stats.new_high_score += 1

            self.stats.highscore = self.stats.aliens_killed
            self.prep_highscore()

    def prep_level(self):
        levels_str = f'Level: {self.stats.level}'
        self.level_image = self.font.render(levels_str, True, self.text_colour)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.midtop = self.kills_rect.midbottom

    def prep_lives(self):
        lives_str = f'Lives: {self.stats.hp_remaining}'
        self.lives_image = self.font.render(lives_str, True, self.text_colour)
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.left = self.screen_rect.left + 10
        self.lives_rect.top = self.kills_rect.top

    def prep_images(self):
        self.prep_kills()
        self.prep_highscore()
        self.prep_level()
        self.prep_lives()

    def show_scoreboard(self):
        self.screen.blit(self.kills_image, self.kills_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.lives_image, self.lives_rect)


