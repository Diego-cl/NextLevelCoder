import pygame
from utils.constants import (
    GREEN,
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_HEIGHT/2
        self.rect.centery = SCREEN_WIDTH/2
    def update(self):
        #self.rect.centerx += 5
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += 5
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
