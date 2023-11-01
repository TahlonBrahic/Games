# standard imports
import pygame

player = pygame.image.load('rouge-like/graphics/fantasy-tileset.png')

def main():
    pygame.init()
    pygame.display.set_caption('rouge-like')

    screen = pygame.display.set_mode((1920,1080))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        scree.blit(player, (50,50))

if __name__ == '__main__':
    main()