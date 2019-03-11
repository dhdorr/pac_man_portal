import pygame
from pygame.sprite import Sprite
from sprite_sheet import SpriteSheet
class TestBlock(Sprite):
    def __init__(self):
        super(TestBlock, self).__init__()

        tb_sprite = SpriteSheet("images/block.png")
        self.image = tb_sprite.get_sprites(0,0,63,63)
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.x = float(self.rect.x)

    def update(self):
        self.rect.x = 100
        self.rect.y = 100

    def blitme(self):
        self.screen.blit(self.image, self.rect)
