import pygame
from pygame.locals import *

# Tileset
image = 'graphics\\fantasy-tileset.png'
tileset = pygame.image.load(image)

# Titleset Definitions
knight = (64, 576, 32, 32)
mage = (32, 576, 32, 32)
rouge = (0, 576, 32, 32)
hunter = (128, 576, 32, 32)

    # Transparent Tiles
background_1 = (0, 0, 32, 32)
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
chest_closed = (0, 128, 32, 32)
chest_opened = (32, 128, 32, 32)

# Map Definitions

    # Starting Room (I would like the same starting room regardless of run.)

starting_room = [
    [wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1],
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],  
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],
    [wall_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, background_1, wall_1],
    [wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1, wall_1]
]

