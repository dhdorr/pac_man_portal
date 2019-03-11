import pygame
from sprite_sheet import SpriteSheet
from settings import Settings

class Portal(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.portal_settings = Settings()

        self.portal1_frames = []
        self.portal2_frames = []

        sprite = SpriteSheet("images/pac_man_portal_ss2.png")

        self.image = sprite.get_sprites(0, 320, 52, 72)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (26,32))
        self.portal1_frames.append(self.image)
        self.image = sprite.get_sprites(52, 320, 52, 72)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (26,32))
        self.portal1_frames.append(self.image)
        self.image = sprite.get_sprites(104, 320, 52, 72)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (26,34))
        self.portal1_frames.append(self.image)
        self.image = sprite.get_sprites(156, 320, 52, 72)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (26,34))
        self.portal1_frames.append(self.image)
        self.image = sprite.get_sprites(0, 392, 52, 72)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (26,34))
        self.portal1_frames.append(self.image)
        self.image = sprite.get_sprites(52, 392, 52, 72)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (26,32))
        self.portal1_frames.append(self.image)
        #Portal 2
        self.image = sprite.get_sprites(104, 392, 52, 72)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (26,32))
        self.portal2_frames.append(self.image)
        self.image = sprite.get_sprites(156, 392, 52, 72)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (26,32))
        self.portal2_frames.append(self.image)
        self.image = sprite.get_sprites(0, 464, 52, 72)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (26,32))
        self.portal2_frames.append(self.image)
        self.image = sprite.get_sprites(52, 464, 52, 72)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (26,32))
        self.portal2_frames.append(self.image)
        self.image = sprite.get_sprites(104, 464, 52, 72)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (26,32))
        self.portal2_frames.append(self.image)
        self.image = sprite.get_sprites(156, 464, 52, 72)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (26,32))
        self.portal2_frames.append(self.image)

        self.portal1_image = self.portal1_frames[0]
        self.portal2_image = self.portal2_frames[0]

        #Get the portal's rect
        self.rect = self.portal1_image.get_rect()
        self.rect2 = self.portal2_image.get_rect()

        self.screen_rect = screen.get_rect()

        #Starting point for portal
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery

        self.rect2.centerx = self.screen_rect.centerx
        self.rect2.bottom = self.screen_rect.centery

        #Portal's center value
        self.center = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        self.center2 = float(self.rect2.centerx)
        self.center2_y = float(self.rect2.centery)

        self.index = 0
        self.spawn_portal = False
        self.spawn_portal2 = False

        self.p1_point = 0
        self.p2_point = 0

    def update(self, frame, player):
        """Spawn n Animate Poratl"""
        #self.rect2.centerx = self. p2_point
        #self.rect.centerx = self.p1_point

        self.index += 1
        if self.index >= len(self.portal1_frames):
            self.index = 0

        self.portal1_image = self.portal1_frames[frame]
        self.portal2_image = self.portal2_frames[frame]
        #print(frame)

    def create_portals(self, player, bullet):

        if not self.spawn_portal and not self.spawn_portal2:
            self.rect.centerx = bullet.rect.x + 16
            self.rect.centery = bullet.rect.y + 16
            self.spawn_portal = True
        elif self.spawn_portal and not self.spawn_portal2:
            self.rect2.centerx = bullet.rect.x + 16
            self.rect2.centery = bullet.rect.y + 16
            self.spawn_portal2 = True
        else:
            self.spawn_portal = False
            self.spawn_portal2 = False

        """if not self.spawn_portal and not self.spawn_portal2:
            if player.face_left:
                self.rect.centerx = (player.rect.centerx - 192)
                self.rect.centery = player.rect.centery
            elif player.face_right:
                self.rect.centerx = (player.rect.centerx + 192)
                self.rect.centery = player.rect.centery
            elif player.face_up:
                self.rect.centerx = player.rect.centerx
                self.rect.centery = (player.rect.centery - 192)
            elif player.face_down:
                self.rect.centerx = player.rect.centerx
                self.rect.centery = (player.rect.centery + 192)
            self.spawn_portal = True
        elif self.spawn_portal and not self.spawn_portal2:
            if player.face_left:
                self.rect2.centerx = (player.rect.centerx - 192)
                self.rect2.centery = player.rect.centery
            elif player.face_right:
                self.rect2.centerx = (player.rect.centerx + 192)
                self.rect2.centery = player.rect.centery
            elif player.face_up:
                self.rect2.centerx = player.rect.centerx
                self.rect2.centery = (player.rect.centery - 192)
            elif player.face_down:
                self.rect2.centerx = player.rect.centerx
                self.rect2.centery = (player.rect.centery + 192)
            self.spawn_portal2 = True
        else:
            self.spawn_portal = False
            self.spawn_portal2 = False"""

    def blitme(self):
        if self.spawn_portal:
            self.screen.blit(self.portal1_image, self.rect)
            if self.spawn_portal2:
                self.screen.blit(self.portal2_image, self.rect2)

