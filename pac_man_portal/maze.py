import pygame
import settings
from sprite_sheet import SpriteSheet
from pygame.sprite import Group
from pygame.sprite import Sprite

class Block(Sprite):
    def __init__(self, x=0, y=0):
        super(Block, self).__init__()
        sprite = SpriteSheet("images/wall_ss2.png")
        self.wallarr = []

        self.image = sprite.get_sprites(0, 0, 32, 32)
        self.image.set_colorkey((0, 0, 0))
        self.wallarr.append(self.image)
        self.image = sprite.get_sprites(32, 0, 32, 32)
        self.image.set_colorkey((0, 0, 0))
        self.wallarr.append(self.image)
        self.image = sprite.get_sprites(0, 32, 32, 32)
        self.image.set_colorkey((0, 0, 0))
        self.wallarr.append(self.image)
        self.image = pygame.transform.rotate(self.wallarr[1], 90)
        self.image.set_colorkey((0,0,0))
        self.wallarr.append(self.image)
        self.image = pygame.transform.rotate(self.wallarr[2], 90)
        self.image.set_colorkey((0, 0, 0))
        self.wallarr.append(self.image)
        self.image = pygame.transform.rotate(self.wallarr[2], 180)
        self.image.set_colorkey((0, 0, 0))
        self.wallarr.append(self.image)
        self.image = pygame.transform.rotate(self.wallarr[2], 270)
        self.image.set_colorkey((0, 0, 0))
        self.wallarr.append(self.image)

        self.rotate = False

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    #def update(self):
        #self.rect.x = 0
        #self.rect.y = 0


class Ball(Sprite):
    def __init__(self,x=0,y=0):
        super(Ball, self).__init__()
        sprite = SpriteSheet("images/pac_ball.png")
        self.balls = []

        self.image = sprite.get_sprites(0,0,32,32)
        self.image = pygame.image.load("images/pac_ball.png")
        self.image = pygame.transform.scale(self.image, (8, 8))
        self.image.set_colorkey((0,0,0))
        self.balls.append(self.image)
        self.image = sprite.get_sprites(0, 0, 32, 32)
        self.image = pygame.image.load("images/pac_ball.png")
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.image.set_colorkey((0, 0, 0))
        self.balls.append((self.image))

        self.rect = self.balls[0].get_rect()
        self.rect.x = x
        self.rect.y = y

        self.points = 10

class Powerup(Sprite):
    def __init__(self, x=0, y=0):
        super(Powerup, self).__init__()
        self.image = pygame.image.load("images/pac_ball.png")
        self.image = pygame.transform.scale(self.image, (20,20))
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.points = 250

class Maze(Sprite):
    def __init__(self, screen, walls, balls, powerups):
        self.offset = 96
        self.M = 19
        self.N = 22
        self.block_list = []
        self.block = Block()
        self.ball = Ball()
        self.maze = [1,4,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,4,1,
                     2,8,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,8,2,
                     2,0,1,1,0,1,4,1,0,2,0,1,4,1,0,1,1,0,2,
                     2,0,1,1,0,1,4,1,0,2,0,1,4,1,0,1,1,0,2,
                     2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,
                     2,0,4,4,0,2,0,4,4,3,4,4,0,2,0,4,4,0,2,
                     2,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,2,
                     1,4,4,1,0,5,4,4,0,2,0,4,4,7,0,1,4,4,1,
                     9,9,9,2,0,2,0,0,0,0,0,0,0,2,0,2,9,9,9,
                     4,4,4,1,0,2,0,1,4,9,4,1,0,2,0,1,4,4,4,
                     0,0,0,0,0,0,0,2,9,9,9,2,0,0,0,0,0,0,0,
                     4,4,4,1,0,2,0,1,4,4,4,1,0,2,0,1,4,4,4,
                     9,9,9,2,0,2,0,0,0,0,0,0,0,2,0,2,9,9,9,
                     1,4,4,1,0,2,0,4,4,3,4,4,0,2,0,1,4,4,1,
                     2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,
                     2,0,4,1,0,4,4,4,0,2,0,4,4,4,0,1,4,0,2,
                     2,0,0,2,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2,
                     5,4,0,2,0,2,0,4,4,3,4,4,0,2,0,2,0,4,7,
                     2,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,2,
                     2,0,4,4,4,6,4,4,0,2,0,4,4,6,4,4,4,0,2,
                     2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,2,
                     1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1]

        bx = 0
        by = 0
        num = 0
        for i in range(0, self.M * self.N):
            if self.maze[bx + (by * self.M)] == 1:
                num = 0
                self.get_block(bx*32, by*32+96, walls, num)
                #wall.rect.x = bx * 64 - 64
                #wall.rect.y = by * 64 - 64
                #screen.blit(self.block.image, (bx * 64, by * 64))
                #walls.add(wall)
            elif self.maze[bx + (by * self.M)] == 2:
                num = 1
                self.get_block(bx*32, by*32+96, walls, num)
            elif self.maze[bx + (by * self.M)] == 3:
                num = 2
                self.get_block(bx*32, by*32+96, walls, num)
            elif self.maze[bx + (by * self.M)] == 4:
                num = 3
                self.get_block(bx*32, by*32+96, walls, num)
            elif self.maze[bx + (by * self.M)] == 5:
                num = 4
                self.get_block(bx*32, by*32+96, walls, num)
            elif self.maze[bx + (by * self.M)] == 6:
                num = 5
                self.get_block(bx*32, by*32+96, walls, num)
            elif self.maze[bx + (by * self.M)] == 7:
                num = 6
                self.get_block(bx*32, by*32+96, walls, num)
            elif self.maze[bx + (by * self.M)] == 8: #balls
                num = 7
                self.get_ball(bx*32+12, by*32+106, balls, num, powerups)
            elif self.maze[bx + (by * self.M)] == 0: #balls
                num = 0
                self.get_ball(bx*32+12, by*32+106, balls, num, powerups)
            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1


    def draw(self, screen, wall, walls, balls, powerups):
        #wall = Block()
        #walllist = []
        bx = 0
        by = 0
        j = 0
        walls.draw(screen)
        balls.draw(screen)
        powerups.draw(screen)
        """
        for i in range(0,self.M*self.N):
            if self.maze[bx + (by*self.M)] == 1:
                #self.get_block(bx*64, by*64, walls)
                #wall.rect.x = bx * 64
                #wall.rect.y = by * 64
                #walllist.append(wall)

                #walllist.append(wall)
                #walls.add(walllist[j])
                #screen.blit(wall.image, wall.rect)
                #screen.blit(self.block.image, (bx*32, by*32+64))
                walls.draw(screen)
                j += 1
            elif self.maze[bx + (by*self.M)] == 2:
                #screen.blit(self.ball.image, (bx*64, by*64))
                balls.draw(screen)
                j += 1
            bx = bx+1
            if bx > self.M-1:
                bx = 0
                by = by + 1
                """

    def get_block(self, xval, yval, walls, num=1):
        myblock = Block(xval, yval)
        myblock.image = myblock.wallarr[num]
        if num == 3:
            myblock.rotate = True

        #wall.rect.x = xval
        #wall.rect.y = yval
        walls.add(myblock)

    def get_ball(self, xval, yval, balls, num, powerups):
        myball = Ball(xval, yval)
        if num == 7:
            mypowup = Powerup(xval, yval)
            powerups.add(mypowup)
        else:
            myball.image = myball.balls[0]
            balls.add(myball)