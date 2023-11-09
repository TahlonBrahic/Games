import pygame
from pygame.locals import *

vec = pygame.math.Vector2

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, tile = 'wall_1'):
        super().__init__()
        self.tile = tile
        self.pos = pos # vec(())

    def collision(self, player):
        if pygame.Rect.colliderect(self.rect, player.rect):
            player.acc = 0
            # Check which side the collision is on, if X is the collision side make self.pos.x = self.pos.x, likewise for y
            if (self.pos.x > 0) and (self.pos.x < 640) and (self.pos.y < 0) and (self.pos.y > 480): # logic that decides whether a block can be moved or not based on where it is
                temp_x = self.pos.x 
                temp_y = self.pos.y
                self.move()
                player.pos.x, player.pos.y = temp_x, temp_y

    def move(self):
        return
