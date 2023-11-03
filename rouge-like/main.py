# standard imports
import pygame
from pygame.locals import *
import player
import assets

# Game Initialization
pygame.init()
pygame.display.set_caption('rouge-like')
screen = pygame.display.set_mode((640,480))
frame_per_second = pygame.time.Clock()
progression_counter = 1 # counts room progression

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
            for row in range(len(assets.starting_room)):
                for column in range(len(assets.starting_room[row])):
                    screen.blit(assets.tileset.subsurface(pygame.Rect(assets.starting_room[row][column])), (row * 32, column * 32)) 

        # print(assets.starting_room[0][0])
        # Time and Frame 
        pygame.display.update()
        frame_per_second.tick(60)

if __name__ == '__main__':
    main()