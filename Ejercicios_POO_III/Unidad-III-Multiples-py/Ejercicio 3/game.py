import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, METEORITO_FREQUENCY
from player import Player
from meteorito import Meteorito

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Nave Espacial vs Meteoritos")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.meteorito = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add()
    
    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if random.randint(1, METEORITO_FREQUENCY) == 1:
                    meteorito = Meteorito()
                    self.all_sprites(meteorito)
                    self.meteorito.add(meteorito)
                self.all_sprites.update()

                if pygame.sprite.spritecollide(self.player, self.meteorito, False):
                    print("GAME OVER")
                    running = False

                self.screen.fill()
                self.all_sprites.draw(self.screen)
                pygame.display.flip()
                    
            
