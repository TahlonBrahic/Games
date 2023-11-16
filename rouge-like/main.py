# standard imports
import pygame, assets, game_entities
from pygame.locals import *

# Game Initialization
assets.graphics.tileset.tileset
pygame.init()
pygame.display.set_caption('rouge-like')
screen = pygame.display.set_mode((640,480), pygame.SCALED)
clock = pygame.time.Clock()
progression_counter = 1 # counts room progression
assets.graphics.tileset.tileset = assets.graphics.tileset.tileset.convert() 

# Room Rendering (can't get this out without circular importing) do I need a room class for generating rooms
def render_room(room):
    for row in range(len(room)):
        for column in range(len(room[row])):
            screen.blit(assets.graphics.tileset.tileset.subsurface(pygame.Rect(room[row][column])), (column * 32, row * 32)) 

# Player
player = game_entities.player.player.Player()
block = game_entities.blocks.block.Block()

# Sprites
sprites = pygame.sprite.Group()
sprites.add(player)
sprites.add(block)

def main():
    running = True

    # Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
                running = False

        # Clear Screen
        screen.fill((0,0,0))

        player.move()
        block.move()
        
        # Drawing Sprites !Need to render sprites above!
        for sprite in sprites:
            screen.blit(sprite.surf, sprite.rect)
        
        # Map Rendering
        if progression_counter == 1:
            render_room(assets.graphics.tileset.starting_room)

        if progression_counter > 1: # start random room generation here
            pass

        # Time and Frame 
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()