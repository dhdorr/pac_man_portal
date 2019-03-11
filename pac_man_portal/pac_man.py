import pygame
import sys
from time import sleep
from player import Player
from portals import Portal
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from maze import Maze, Block
from ghost import Ghost
from stats import Stats
from scoreboard import Scoreboard
from sprite_sheet import SpriteSheet

clock = pygame.time.Clock()

def run_game():
    pygame.init()
    pmp_settings = Settings()
    screen = pygame.display.set_mode((pmp_settings.screen_width, pmp_settings.screen_height))
    pygame.display.set_caption("Pac Man Portal")
    walls = Group()
    wall = Block()
    balls = Group()
    ghost = Ghost(screen)
    ghosts = Group()
    ghosts.add(ghost)
    bullets = Group()
    powerups = Group()

    stats = Stats(pmp_settings)
    sb = Scoreboard(screen, stats, pmp_settings)

    map = Maze(screen, walls, balls, powerups)
    #block = pygame.image.load("images/block.png").convert()
    #block.set_colorkey((0,0,0))

    player = Player(screen)
    p_group = Group()
    p_group.add(player)
    portals = Portal(screen)

    start_screen(screen, stats)

    clock = pygame.time.Clock()
    nextFrame = pygame.time.get_ticks()
    nextFrame2 = nextFrame
    frame = 0
    frame2 = 0

    strt_ticks = pygame.time.get_ticks()
    waitme = True

    while True:
        if pygame.time.get_ticks() > nextFrame:
            frame = (frame+1)%10
            #frame2 = (frame2+1)%6
            nextFrame += 60
        if pygame.time.get_ticks() > nextFrame2:
            frame2 = (frame2 + 1) % 6
            nextFrame2 += 140

        seconds = (pygame.time.get_ticks()-strt_ticks)/1000
        #if seconds >= .5:
            #player.update(frame, portals)
        player.update(frame, portals, walls, p_group, balls, stats, sb, powerups, ghosts)
        ghosts.update(player)
        gf.update_bullets(bullets, player, walls, portals)
        if portals.spawn_portal:
            portals.update(frame2, player)
            
        gf.check_events(player, portals, screen, walls, bullets)
        gf.update_screen(player, screen, pmp_settings, portals, map, wall, walls, balls, ghosts, bullets, sb, powerups)
        if waitme:
            sleep(3.5)
            waitme = False
            nextFrame = strt_ticks

        clock.tick(120)

def start_screen(screen, stats):
    intro_song = pygame.mixer.Sound("songs/pac_intro.wav")
    """Start Screen"""
    pac_image = pygame.image.load("images/smollest_pacman.png")
    sprite = SpriteSheet("images/pac_man_portal_ss2.png")
    port_image = sprite.get_sprites(0, 320, 52, 72)
    port_image2 = sprite.get_sprites(0, 464, 52, 72)
    port_image.set_colorkey((0, 0, 0))
    port_image2.set_colorkey((0,0,0))
    while(stats.game_active == False):
        screen.fill((0,0,0))
        myfont = pygame.font.SysFont("Britannic Bold", 100)
        startfont = pygame.font.SysFont("Britannic Bold", 32)
        label = myfont.render("PAC-MAN", 1, (250,250,250))
        label2 = myfont.render("PORTAL", 1, (100, 200, 200))
        label3 = startfont.render("CLICK TO START", 1, (200, 200, 200))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                stats.game_active = True
                intro_song.play()
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(label, (124,100))
        screen.blit(label2, (148,164))
        screen.blit(label3, (200,600))
        screen.blit(pac_image, (260, 124))
        screen.blit(port_image, (90, 170))
        screen.blit(port_image2, (428, 170))
        pygame.display.flip()
        sleep(1.0)


run_game()


