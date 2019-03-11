import pygame.font
from pygame.sprite import Group
from player import Player

class Scoreboard():
    def __init__(self, screen, stats, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.pac_settings = settings

        self.text_color = (250,250,250)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_pacs()

        self.score_txt = self.font.render("Game Score:", True, (40,110,150), self.pac_settings.bg_color)
        self.score_txt_rect = self.score_txt.get_rect()
        self.score_txt_rect.right = self.screen_rect.right - 20
        self.score_txt_rect.top = 12

    def prep_score(self):
        score = self.stats.score
        score_str = "{:,}".format(score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.pac_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 25
        self.score_rect.top = 55

    def prep_high_score(self):
        high_score = self.stats.high_score
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.pac_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_pacs(self):
        self.pacs = Group()
        for pac_num in range(self.stats.pacs_left):
            pacman = Player(self.screen)
            pacman.rect.x = 10 + (pac_num * (pacman.rect.width * 2))
            pacman.rect.y = self.screen_rect.bottom -86
            self.pacs.add(pacman)

    def show_score(self):
        self.screen.blit(self.score_txt, self.score_txt_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.pacs.draw(self.screen)