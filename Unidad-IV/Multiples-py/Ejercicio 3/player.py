import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2 # aparece al medio de la pantalla
        self.rect.bottom = SCREEN_HEIGHT - 10
        
        pygame.draw.polygon(self.image, (0, 0, 255), [(25, 0), (0, 50), (50, 50)])

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if self.rect.left < 0:
            self.rect.left = 0 
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            