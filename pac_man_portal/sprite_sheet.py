import pygame

class SpriteSheet(object):
    def __init__(self, file_name="images/pac_man_portal_ss2.png"):
        self.sprite_sheet = pygame.image.load(file_name).convert()
        bg_color = (0,0,0)

    def get_sprites(self, x, y, width, height):
        sprite = pygame.Surface([width, height]).convert()
        sprite.blit(self.sprite_sheet, (0,0), (x,y,width,height))
        return sprite