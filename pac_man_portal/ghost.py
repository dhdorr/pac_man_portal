import pygame
from sprite_sheet import SpriteSheet
from settings import Settings
from maze import Maze, Block
from pygame.sprite import Sprite
from pygame.sprite import Group
from player import Player

class Ghost(Sprite):
    def __init__(self, screen):
        super(Ghost, self).__init__()
        self.screen = screen
        self.g_settings = Settings()
        self.ghost_frames = []

        #sprite = SpriteSheet("images/ghost_pmp.png")

        #self.image = sprite.get_sprites(0, 0, 64, 64)
        #self.image.set_colorkey((0, 0, 0))
        #self.ghost_frames.append(self.image)

        #self.ghost_image = self.ghost_frames[0]
        self.image = pygame.image.load("images/ghost_pmp.png")
        self.image = pygame.transform.scale(self.image, (32,32))

        self.rect = self.image.get_rect()

        self.rect.x = 304
        self.rect.y = 416

    def update(self, player):
        if player.rect.x > 304:
            self.rect.x += self.g_settings.ghost_speed
            if self.rect.x > 608:
                self.rect.x = -20
            #self.rect.y -= self.g_settings.ghost_speed
        elif player.rect.x <= 304:
            self.rect.x -= self.g_settings.ghost_speed
            if self.rect.x < 0:
                self.rect.x = 608
            #self.rect.y -= self.g_settings.ghost_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)