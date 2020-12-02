import pygame
from utils.constants import (
    GREEN,
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)
from components.bullet import Bullet
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.bullets = pygame.sprite.Group()


    def update(self):
        #self.rect.centerx += 5
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if key[pygame.K_LEFT]:
            self.rect.x += -5

        if self.rect.left <= 0:
            self.rect.left = 0


    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.game.all_sprites.add(bullet)
        self.bullets.add(bullet)




