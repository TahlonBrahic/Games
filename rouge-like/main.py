# standard imports
import pygame
from pygame.locals import *
import game_entities.player as player
import assets.graphics.assets as assets

# Game Initialization
pygame.init()
pygame.display.set_caption('rouge-like')
screen = pygame.display.set_mode((640,480))
frame_per_second = pygame.time.Clock()
progression_counter = 1 # counts room progression

# Room Rendering (can't get this out without circular importing)
def render_room(room):
    for row in range(len(room)):
        for column in range(len(room[row])):
            screen.blit(assets.tileset.subsurface(pygame.Rect(room[row][column])), (column * 32, row * 32)) 

# Player
player = player.Player()

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

        # Clear Screen
        screen.fill((0,0,0))

        player.move()
        
        # Drawing Sprites
        for sprite in sprites:
            screen.blit(sprite.surf, sprite.rect)
        
        # Map Rendering
        if progression_counter == 1:
            render_room(assets.starting_room)

        if progression_counter > 1: # start random room generation here
            pass

        # Time and Frame 
        pygame.display.update()
        frame_per_second.tick(60)

if __name__ == '__main__':
    main()