import pygame, sys, os
from pygame.locals import *

assets_path = os.path.abspath('C:/Users/Tahlon/Documents/Programming/Games/rouge-like/assets/Graphics')
sys.path.append(assets_path)

import assets 

vec = pygame.math.Vector2

class Block(pygame.sprite.Sprite):
    def __init__(self, pos = (100, 100), image = assets.wall_1): # assets.tileset.subsurface(pygame.Rect(self.player_class))
        super().__init__()
        self.image = image
        self.surf = assets.tileset.subsurface(pygame.Rect(self.image))
        self.rect = self.surf.get_rect()
        self.pos = vec(pos)

    def move(self): # This is temp code to test the move function
        temp = pygame.key.get_pressed()
        if temp[K_0]:
            self.pos += 1

