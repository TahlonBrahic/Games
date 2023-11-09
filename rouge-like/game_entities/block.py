import pygame
from pygame.locals import *

vec = pygame.math.Vector2

class Block(pygame.sprite.Sprite):
    def __init__(self, tile = 'wall_1', pos):
        super().__init__()
        self.tile = tile
        self.pos = pos # vec(())

    def collision(self, player):
        if pygame.Rect.colliderect(self.rect, player.rect):
            player.acc = 0
            # Check which side the collision is on, if X is the collision side make self.pos.x = self.pos.x, likewise for y

    def move(self):
        return
