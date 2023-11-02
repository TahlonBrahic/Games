# standard imports
import pygame
from pygame.locals import *

# Game Initialization
pygame.init()
pygame.display.set_caption('rouge-like')
screen = pygame.display.set_mode((640,480))

# Game Variables
vec = pygame.math.Vector2
ACC = 0.5
FRIC = -0.12
frame_per_second = pygame.time.Clock()
 
# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, player_class='knight'):
        super().__init__()
        self.player_class = player_class
        self.surf = self.player_model()
        self.rect = self.surf.get_rect()
        # Movement variables
        self.pos = vec((320, 240))
        self.vel = vec((0,0))
        self.acc = vec((0,0))

    def player_model(self):
        if self.player_class == 'knight':
            tileset = pygame.image.load('graphics/fantasy-tileset.png')
            player_model = tileset.subsurface(pygame.Rect(64, 576, 32, 32)) # because this is a 32x32 tileset you can scroll over with 8-bit adjustments to the first two parameters, the first is row, the second is column
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
        if pressed_keys[K_d]:
            self.acc.y = ACC
            

        # Equation of motion for de-acceleration
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Entering another room (screen warping)
        if self.pos.x > 640:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = 640

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