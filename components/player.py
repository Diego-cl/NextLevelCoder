import pygame

from utils.constants import (
    BLACK,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    IMG_DIR
)
from components.bullet import Bullet
from os import path
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(path.join(IMG_DIR, "alien.png")).convert()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.bullets = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()


    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if key[pygame.K_LEFT]:
            self.rect.x += -5

        if self.rect.left <= 0:
            self.rect.left = 0


    def shoot(self, colision):
        sound_rifle = pygame.mixer.Sound(path.join(IMG_DIR, "rifle.ogg"))
        pygame.mixer.Sound.play(sound_rifle)
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.game.all_sprites.add(bullet)
        self.bullets.add(bullet)

        colision_c = colision


        if colision == True:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet1 = Bullet(self.rect.centerx - 10, self.rect.top)
            bullet2 = Bullet(self.rect.centerx -20, self.rect.top)
            bullet3 = Bullet(self.rect.centerx + 10, self.rect.top)
            bullet4 = Bullet(self.rect.centerx + 20, self.rect.top)
            self.game.all_sprites.add(bullet)
            self.game.all_sprites.add(bullet1)
            self.game.all_sprites.add(bullet2)
            self.game.all_sprites.add(bullet3)
            self.game.all_sprites.add(bullet4)



