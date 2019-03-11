import pygame
import sys
#from player import Player
from p_bullet import Bullet

"""CLOCK and TIMERS"""
def clock():
    current_time = pygame.time.get_ticks()
    return current_time

"""Events Block"""
def check_events(player, portals, screen, walls, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_kd_events(player, event, portals, screen, walls, bullets)
        elif event.type == pygame.KEYUP:
            check_ku_events(player, event)

def check_kd_events(player, event, portals, screen, walls, bullets):
    if event.key == pygame.K_RIGHT:
        player.move_right = True
        player.move_up = False
        player.move_left = False
        player.move_down = False
        player.face_left = False
        player.face_up = False
        player.face_down = False
        player.face_right = True
        #player.move_left = False
        #print("Moving Right")
    elif event.key == pygame.K_LEFT:
        player.move_left = True
        player.move_up = False
        player.move_down = False
        player.move_right = False
        player.face_right = False
        player.face_up = False
        player.face_down = False
        player.face_left = True
        #player.move_right = False
        #print("Moving Left")
    elif event.key == pygame.K_UP:
        player.move_up = True
        player.move_down = False
        player.move_left = False
        player.move_right = False
        player.face_right = False
        player.face_left = False
        player.face_down = False
        player.face_up = True
    elif event.key == pygame.K_DOWN:
        player.move_down = True
        player.move_up = False
        player.move_left = False
        player.move_right = False
        player.face_right = False
        player.face_left = False
        player.face_up = False
        player.face_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(screen, player, walls)
        if player.face_right:
            new_bullet.direction = 0
        elif player.face_left:
            new_bullet.direction = 1
        elif player.face_up:
            new_bullet.direction = 2
        elif player.face_down:
            new_bullet.direction = 3
        bullets.add(new_bullet)
        #portals.create_portals(player)

def check_ku_events(player, event):
    if event.key == pygame.K_RIGHT:
        #print("hi")
        player.move_right = False
    elif event.key == pygame.K_LEFT:
        #print("hi")
        player.move_left = False
    elif event.key == pygame.K_UP:
        player.move_up = False
    elif event.key == pygame.K_DOWN:
        player.move_down = False

def update_screen(player, screen, pmp_settings, portals, map, wall, walls, balls, ghosts, bullets, sb, powerups):
    screen.fill(pmp_settings.bg_color)
    map.draw(screen, wall, walls, balls, powerups)

    sb.show_score()

    player.blitme()
    ghosts.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    portals.blitme()

    pygame.display.flip()

def update_bullets(bullets, player, walls, portals):
    bullets.update(player)
    collision = pygame.sprite.groupcollide(bullets, walls, True, False)
    for wall in collision.values():
        portals.create_portals(player, wall[0])

    for bullet in bullets.copy():
        if bullet.rect.top <= 0 or bullet.rect.top >= 900:
            bullets.remove(bullet)
            print("GONE")
        elif bullet.rect.x <= 0 or bullet.rect.x >= 600:
            bullets.remove(bullet)
            print("GONE")
        elif pygame.sprite.groupcollide(bullets, walls, True, False):
            print("HIT")

def reset_ghosts(ghosts):
    for ghost in ghosts:
        ghost.rect.x = 304
        ghost.rect.y = 416