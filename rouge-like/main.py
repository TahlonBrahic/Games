# standard imports
import pygame
from pygame.locals import *

# Game Initialization
pygame.init()
pygame.display.set_caption('rouge-like')
screen = pygame.display.set_mode((640,480))

# Game Variables
vec = pygame.math.Vector2py
ACC = 0.5
FRIC = -0.12
frame_per_second = pygame.time.Clock()

# Titleset Definitions

    # Characters
knight = (64, 576, 32, 32)
mage = (32, 576, 32, 32)
rouge = (0, 576, 32, 32)
hunter = (128, 576, 32, 32)

    # Transparent Tiles
transparent_background_1 = (0, 0, 32, 32)
transparent_background_2 = (32, 0, 32, 32)
transparent_background_3 = (64, 0, 32, 32)
transparent_background_4 = (96, 0, 32, 32)
transparent_background_5 = (128, 0, 32, 32)
transparent_background_6 = (160, 0, 32, 32)
transparent_background_7 = (192, 0, 32, 32)
transparent_background_8 = (224, 0, 32, 32)

    # Walls
wall_1 = (0, 32, 32, 32)
wall_2 = (32, 32, 32, 32)
wall_3 = (64, 32, 32, 32)
wall_4 = (96, 32, 32, 32) # cracked wall
wall_5 = (128, 32, 32, 32)
wall_6 = (160, 32, 32, 32) # stairs down
wall_7 = (192, 32, 32, 32) # stairs up
wall_8 = (224, 32, 32, 32) # pit
wall_9 = (0, 64, 32, 32)
wall_10 = (32, 64, 32, 32)
wall_11 = (64, 64, 32, 32) # brick
wall_12 = (96, 64, 32, 32) # brick
wall_13 = (128, 64, 32, 32) # secret room
wall_14 = (160, 64, 32, 32) # door
wall_15 = (192, 64, 32, 32) # door
wall_16 = (224, 64, 32, 32) 

    # Assets
chest = (0, 128, 32, 32)

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, player_class=chest):
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

# Player
player = Player()

# Sprites
sprites = pygame.sprite.Group()
sprites.add(player)

def main():
    running = True

    # Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill((0,0,0))

        player.move()
        
        # Drawing Sprites
        for sprite in sprites:
            screen.blit(sprite.surf, sprite.rect)
        
        player.move()

        # Time and Frame 
        pygame.display.update()
        frame_per_second.tick(60)

if __name__ == '__main__':
    main()