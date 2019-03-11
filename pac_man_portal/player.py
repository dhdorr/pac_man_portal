import pygame
import sys

from sprite_sheet import SpriteSheet
from settings import Settings
from maze import Maze, Block
from pygame.sprite import Sprite
from pygame.sprite import Group
from time import sleep
import game_functions as gf

class Player(Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        self.player_frames = []
        self.p_die_frames = []
        self.pmp_settings = Settings()
        self.screen = screen
        #self.maze = Maze()

        sprite = SpriteSheet("images/pac_man_portal_ss2.png")
        #sprite = pygame.transform.scale(sprite, (44,44))

        #image = sprite.get_sprites(0,0,48,48)
        #self.image = pygame.image.load("images/pac_man_portal_ss2.png")
        #self.image = pygame.transform.scale(self.image, (38,38))
        #self.image.set_colorkey((0,0,0))
        #self.player_frames.append(self.image)

        self.image = sprite.get_sprites(0, 0, 64, 64)
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.scale(self.image, (38,38))
        self.player_frames.append(self.image)
        #self.image = sprite.get_sprites(0, 128, 64, 64)
        self.image = sprite.get_sprites(64, 0, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38,38))
        self.player_frames.append(self.image)
        #self.image = sprite.get_sprites(64, 0, 64, 64)
        self.image = sprite.get_sprites(128, 0, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38,38))
        self.player_frames.append(self.image)
        self.image = sprite.get_sprites(0, 64, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38,38))
        self.player_frames.append(self.image)
        self.image = sprite.get_sprites(64, 64, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38,38))
        self.player_frames.append(self.image)
        self.image = sprite.get_sprites(128, 64, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38, 38))
        self.player_frames.append(self.image)
        #reverse
        self.image = sprite.get_sprites(64, 64, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38,38))
        self.player_frames.append(self.image)
        self.image = sprite.get_sprites(0, 64, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38,38))
        self.player_frames.append(self.image)
        self.image = sprite.get_sprites(128, 0, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38,38))
        self.player_frames.append(self.image)
        self.image = sprite.get_sprites(64, 0, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38,38))
        self.player_frames.append(self.image)

        """Death Animation"""
        self.image = sprite.get_sprites(128, 0, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38, 38))
        self.p_die_frames.append(self.image)
        self.image = sprite.get_sprites(64, 0, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38, 38))
        self.p_die_frames.append(self.image)
        self.image = sprite.get_sprites(0, 0, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38, 38))
        self.p_die_frames.append(self.image)
        self.image = sprite.get_sprites(64, 128, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38, 38))
        self.p_die_frames.append(self.image)
        self.image = sprite.get_sprites(128, 128, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38, 38))
        self.p_die_frames.append(self.image)
        self.image = sprite.get_sprites(0, 192, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38, 38))
        self.p_die_frames.append(self.image)
        self.image = sprite.get_sprites(64, 192, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38, 38))
        self.p_die_frames.append(self.image)
        self.image = sprite.get_sprites(128, 192, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38, 38))
        self.p_die_frames.append(self.image)
        self.image = sprite.get_sprites(0, 256, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38, 38))
        self.p_die_frames.append(self.image)
        self.image = sprite.get_sprites(64, 256, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38, 38))
        self.p_die_frames.append(self.image)
        self.image = sprite.get_sprites(128, 256, 64, 64)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (38, 38))
        self.p_die_frames.append(self.image)


        self.player_image = self.player_frames[0]

        #Get the player's rect
        self.rect = self.player_frames[0].get_rect(size=(24,24))
        #self.rect = pygame.rect.Rect((300,412,24,24))
        #self.rect.width -= 4
        #self.rect.height -= 4
        self.screen_rect = screen.get_rect()

        #Starting point for player
        #self.rect.centerx = self.screen_rect.centerx
        #self.rect.bottom = self.screen_rect.centery
        self.rect.centerx = 304
        self.rect.bottom = 416

        #Player's center value
        self.center = float(self.rect.centerx)
        self.center_y = float(self.rect.centery) + 96

        #self.rect.centerx -= 6
        #self.rect.centery -= 6
        
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        self.face_right = False
        self.face_left = False
        self.face_up = False
        self.face_down = False

        self.teleported = False
        self.start_ticks = 0
        
        self.index = 0

    def update(self, frame, portals, walls, p_group, balls, stats, sb, powerups, ghosts):

        collision = pygame.sprite.groupcollide(p_group, walls, False, False)
        if collision:
            print("Yay")

        collision2 = pygame.sprite.groupcollide(p_group, balls, False, True)
        if collision2:
            stats.score += 10
            sb.prep_score()
            print("BALL")

        collision3 = pygame.sprite.groupcollide(p_group, powerups, False, True)
        if collision3:
            stats.score += 250
            sb.prep_score()
            print("POWERUP")

        collision4 = pygame.sprite.groupcollide(p_group, ghosts, False, False)
        if collision4:
            self.kill_player(stats, sb, ghosts)
            print("Life Lost!")

        if not collision:
            """Movement and bounds"""
            if self.move_right:
                if self.rect.left > self.screen_rect.right:
                    self.center = self.screen_rect.left - 32
                self.center += self.pmp_settings.player_speed
            if self.move_left:
                if self.rect.right < self.screen_rect.left:
                    self.center = self.screen_rect.right + 32
                self.center -= self.pmp_settings.player_speed
            if self.move_up and self.rect.top > self.screen_rect.top:
                self.center_y -= self.pmp_settings.player_speed
            if self.move_down and self.rect.bottom < self.screen_rect.bottom:
                self.center_y += self.pmp_settings.player_speed
        elif collision:
            if self.move_right:
                self.center -= 2
                self.move_right = False
                #self.center -= 2
            elif self.move_left:
                self.center +=2
                self.move_left = False
                #self.center +=2
            elif self.move_up:
                self.center_y += 2
                self.move_up = False
                #self.center_y += 2
            elif self.move_down:
                self.center_y -=2
                self.move_down = False
                #self.center_y -= 2

        """Move Thru Portals"""
        if portals.spawn_portal and portals.spawn_portal2 and not self.teleported:
            if self.center >= portals.rect2.centerx-32 and self.center <= portals.rect2.centerx+32:
                if self.center_y >= portals.rect2.centery-32 and self.center_y <= portals.rect2.centery+32:
                    self.center = portals.rect.centerx - 32
                    self.center_y = portals.rect.centery
                    self.teleported = True
                    self.start_ticks = pygame.time.get_ticks()
                    #portals.spawn_portal2 = False
                    #portals.spawn_portal = False
            elif self.center >= portals.rect.centerx-32 and self.center <= portals.rect.centerx+32:
                if self.center_y >= portals.rect.centery-32 and self.center_y <= portals.rect.centery+32:
                    self.center = portals.rect2.centerx - 32
                    self.center_y = portals.rect2.centery
                    self.teleported = True
                    self.start_ticks = pygame.time.get_ticks()
                    #portals.spawn_portal2 = False
                    #portals.spawn_portal = False

        if self.teleported:
            seconds = (pygame.time.get_ticks()-self.start_ticks)/1000
            #print(3-int(seconds), "SECONDS LEFT!")
            if seconds >= 2:
                self.teleported = False

        self.rect.centerx = self.center
        self.rect.centery = self.center_y

        self.index += 1
        if self.index >= len(self.player_frames):
            self.index = 0

        self.image = self.player_frames[frame]
        #print(frame)


    def kill_player(self, stats, sb, ghosts):
        clock = pygame.time.Clock()
        nextFrame = 0
        frame = 0
        i = 0
        if stats.pacs_left > 0:
            stats.pacs_left -= 1
            for i in range(11):
                self.image = self.p_die_frames[i]
                self.rect.centerx = self.center
                self.rect.centery = self.center_y
                self.blitme()
                pygame.display.flip()
                frame += 1
                clock.tick(12)
            sb.prep_pacs()
        else:
            print("Game Over!")
            ghosts.empty()
            stats.game_active = False

        sleep(0.75)
        self.center = 304
        self.center_y = 498
        gf.reset_ghosts(ghosts)


    def blitme(self):
        if self.face_right:
            self.screen.blit(pygame.transform.flip(self.image, 1, 0), self.rect.move(-6,-6))
        elif self.face_up:
            self. screen.blit(pygame.transform.rotate(self.image, -90), self.rect.move(-6,-6))
        elif self.face_down:
            self. screen.blit(pygame.transform.rotate(self.image, 90), self.rect.move(-6,-6))
        else :
            self.screen.blit(self.image, self.rect.move(-6,-6))



"""TESTING
        tb = TestBlock()
        tb2 = TestBlock()
        tb3 = TestBlock()
        tb_group = Group()
        tb_list = []
        tb_list.append(tb)
        #tb_group.add(tb_list)
        tb2.rect.x = 200
        tb2.rect.y = 100
        tb_list.append(tb2)
        #tb_group.add(tb2)
        tb3.rect.x = 400
        tb3.rect.y = 100
        tb_list.append(tb3)
         for i in range(3):
            tb_group.add(tb_list[i])"""