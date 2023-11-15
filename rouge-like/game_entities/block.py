import pygame
from pygame.locals import *

vec = pygame.math.Vector2

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, image = 'wall_1'):
        super().__init__()
        self.image = image
        self.pos = pos # vec(())
        self.rect = self.image.get_rect()

    def move(self):
        return
    # I need logic to check collision side to be able to tell move() where to move the block
