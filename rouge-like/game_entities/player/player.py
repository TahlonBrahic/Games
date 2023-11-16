import pygame, sys, os
from pygame.locals import *

assets_path = os.path.abspath('C:/Users/Tahlon/Documents/Programming/Games/rouge-like/assets/graphics')
sys.path.append(assets_path)

import assets.graphics.tileset as assets

# Physics Variables
vec = pygame.math.Vector2
ACC = 0.5
FRIC = -0.20

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, player_class=assets.knight):
        super().__init__()
        self.player_class = player_class
        self.surf = assets.tileset.subsurface(pygame.Rect(self.player_class))
        self.rect = self.surf.get_rect()
        # Movement variables
        self.pos = vec((320, 240))
        self.vel = vec((0,0))
        self.acc = vec((0,0))
      
    def move(self):
        # Resets player acceleration to 0
        self.acc = vec((0,0))

        # Obtain list of pressed keys
        pressed_keys = pygame.key.get_pressed()

        # Movement
        if pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_d]:
            self.acc.x = ACC
        if pressed_keys[K_w]:
            self.acc.y = -ACC
        if pressed_keys[K_s]:
            self.acc.y = ACC
            
        # Equation of motion for de-acceleration
        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Bounding 
        if (self.pos.x > 600):
            self.acc = 0
            self.pos.x = 600
        if (self.pos.x < 40):
            self.acc = 0
            self.pos.x = 40
        if (self.pos.y > 450):
            self.acc = 0
            self.pos.y = 450
        if (self.pos.y < 60):
            self.acc = 0
            self.pos.y = 60

        self.rect.midbottom = self.pos