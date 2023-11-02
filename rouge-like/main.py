# standard imports
import pygame

pygame.init()
pygame.display.set_caption('rouge-like')
screen = pygame.display.set_mode((640,480))
frame_per_second = pygame.time.Clock()
 
 # Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, player_class='knight'):
        super().__init__()
        self.surf = pygame.Surface((30,30))
        self.rect = self.surf.get_rect()
        self.player_class = player_class

    def player_model(self):
        if self.player_class == 'knight':
            tileset = pygame.image.load('graphics/fantasy-tileset.png')
            player_model = tileset.subsurface(pygame.Rect(64, 576, 32, 32)) # because this is a 32x32 tileset you can scroll over with 8-bit adjustments to the first two parameters, the first is row, the second is column
            return player_model

     

def main():
    running = True

    # Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Drawing Entities
        screen.blit(Player().player_model(), (320,200))

        # Time and Frame 
        pygame.display.update()
        frame_per_second.tick(60)

if __name__ == '__main__':
    main()