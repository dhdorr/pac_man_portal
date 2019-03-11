import pygame
from pygame.sprite import Sprite
import random


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, screen, player, walls):
        """Create a bullet object, at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, 6, 4)
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top

        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)

        self.color = (250,250,250)
        self.speed_factor = 3
        
        self.fire_left = False
        self.direction = 0

    def update(self, player):
        if self.direction == 1:
            self.rect.x -= self.speed_factor
            """Move the bullet up the screen."""
            # Update the decimal position of the bullet.
        elif self.direction == 2:
            self.y -= self.speed_factor
            # Update the rect position.
            self.rect.y = self.y
        elif self.direction == 0:
            self.rect.x += self.speed_factor
        elif self.direction == 3:
            self.rect.y += self.speed_factor

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)