import pygame
from pygame.locals import *
import assets

# Physics Variables
vec = pygame.math.Vector2
ACC = 0.5
FRIC = -0.12

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, player_class=assets.knight):
        super().__init__()
        self.player_class = player_class
        self.surf = self.player_model()
        self.rect = self.surf.get_rect()
        # Movement variables
        self.pos = vec((320, 240))
        self.vel = vec((0,0))
        self.acc = vec((0,0))

    def player_model(self):
        tileset = pygame.image.load('graphics/fantasy-tileset.png')
        player_model = tileset.subsurface(pygame.Rect(self.player_class)) # because this is a 32x32 tileset you can scroll over with 8-bit adjustments to the first two parameters, the first is row, the second is column
        return player_model
        
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

        # Entering another room (screen warping) of course there would need to be a door but that can be added later
        if self.pos.x > 640:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = 640
        if self.pos.y > 480:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = 480

        self.rect.midbottom = self.pos