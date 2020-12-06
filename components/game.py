import pygame

from components.powerup import Powerup
from components.ball import Ball
from components.player import Player
from utils.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    IMG_DIR,
    WHITE,
    GREEN
)
from os import path
from utils.text_utils import draw_text

def dr_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def draw_hp(surface, x, y, percentage):
    BAR_LENGHT = 100
    BAR_HEIGHT = 10
    fill = (percentage / 100) * BAR_LENGHT
    borde = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surface, GREEN, fill)
    pygame.draw.rect(surface, WHITE, borde, 4)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_img = pygame.image.load(path.join(IMG_DIR, "spacefield.png")).convert()
        self.background_img = pygame.transform.scale(self.background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = True
        self.colision = False
        self.hp = 100
        self.score = 0
        pygame.mixer.init()
        pygame.mixer.music.load(path.join(IMG_DIR, "town4.mp3"))
        pygame.mixer.music.play(-1)


    def run(self):
        self.create_components()
        #Game loop:
        self.playing = True
        while self.playing:
            self.clock.tick(30)
            self.events()
            self.update()
            self.draw()


    def create_components(self):
        self.all_sprites = pygame.sprite.Group()

        self.balls = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.player.hp = Player(self)

        ball = Ball(1)
        self.all_sprites.add(ball)
        self.balls.add(ball)

        self.powerups = pygame.sprite.Group()
        powerup = Powerup()
        self.all_sprites.add(powerup)
        self.powerups.add(powerup)


    def update(self):
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player, self.balls, False)
        for hit in hits:
            self.hp -= 25
            if self.hp <= 0:
                self.playing = False
        hits = pygame.sprite.groupcollide(self.balls, self.player.bullets, True, True)

        for hit in hits:
            self.score += 10
            if hit.size < 4:
                for i in range(0, 3):
                    ball = Ball(hit.size + 1)
                    self.all_sprites.add(ball)
                    self.balls.add(ball)
        hits = pygame.sprite.spritecollide(self.player, self.powerups, True)
        if hits:
            self.colision = True


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot(self.colision)


    def draw(self):
        background_rect = self.background_img.get_rect()
        self.screen.blit(self.background_img, background_rect)
        self.all_sprites.draw(self.screen)
        dr_text(self.screen, str(self.score), 25, SCREEN_WIDTH // 2, 10)
        draw_hp(self.screen, 670, 20, self.hp)
        pygame.display.flip()


    def show_start_screen(self):
        self.screen.blit(self.background_img, self.background_img.get_rect())
        draw_text(self.screen, " Game Working !!", 64, SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
        draw_text(self.screen, "presiona las teclas direccionales y SPACE para disparar", 20,
                  SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        draw_text(self.screen, "press ENTER key to begin", 20, SCREEN_WIDTH/2, SCREEN_HEIGHT*3/5)
        pygame.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        waiting = False






