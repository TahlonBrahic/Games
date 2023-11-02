# standard imports
import pygame

def choose_player_character(player_class='knight'):
    if player_class == 'knight':
        tileset = pygame.image.load('graphics/fantasy-tileset.png')
        player_model = tileset.subsurface(pygame.Rect(0, 0, 32, 32))
        return player_model

player = choose_player_character()        

def main():
    pygame.init()
    pygame.display.set_caption('rouge-like')

    screen = pygame.display.set_mode((1920,1080))

    running = True

    # Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
        screen.fill((255, 255, 255))
        
        screen.blit(player, (400,300))

if __name__ == '__main__':
    main()