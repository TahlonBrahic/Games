# standard imports
from typing import Union
import pygame
from sys import exit
from random import randint
from pygame.surface import Surface, SurfaceType

# boiler plate
pygame.init()
screen: Union[Surface, SurfaceType] = pygame.display.set_mode((800, 400))
pygame.display.set_caption('rouge-like')
clock = pygame.time.Clock()
game_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
