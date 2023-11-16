import pygame, sys, os
from pygame.locals import *

assets_path = os.path.abspath('C:/Users/Tahlon/Documents/Programming/Games/rouge-like/assets/graphics')
sys.path.append(assets_path)

import assets.graphics.tileset as assets

vec = pygame.math.Vector2
ACC = 0.5
FRIC = -0.12

class Block(pygame.sprite.Sprite):
    def __init__(self, pos = (300, 200), image = assets.wall_14): # assets.tileset.subsurface(pygame.Rect(self.player_class))
        super().__init__()
        self.image = image
        self.surf = assets.tileset.subsurface(pygame.Rect(self.image))
        self.rect = self.surf.get_rect()
        self.pos = vec(pos)
        self.vel = vec((0,0))
        self.acc = vec((0,0))

    # def move(self): # This is temp code to test the move function
    #     # Resets player acceleration to 0
    #     self.acc = vec((0,0))

    #     # Obtain list of pressed keys
    #     pressed_keys = pygame.key.get_pressed()

    #     # Movement
    #     if pressed_keys[K_UP]:
    #         self.acc.x = -ACC
    #     if pressed_keys[K_DOWN]:
    #         self.acc.x = ACC

            
    #     # Equation of motion for de-acceleration
    #     self.acc.x += self.vel.x * FRIC
    #     self.acc.y += self.vel.y * FRIC
    #     self.vel += self.acc
    #     self.pos += self.vel + 0.5 * self.acc

    #     # Bounding for play inside room. I might replace this with the block class
    #     if (self.pos.x > 600):
    #         self.acc = 0
    #         self.pos.x = 600
    #     if (self.pos.x < 40):
    #         self.acc = 0
    #         self.pos.x = 40
    #     if (self.pos.y > 450):
    #         self.acc = 0
    #         self.pos.y = 450
    #     if (self.pos.y < 60):
    #         self.acc = 0
    #         self.pos.y = 60

    #     self.rect.midbottom = self.pos