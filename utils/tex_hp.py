import pygame
from utils.constants import (
    GREEN,
    WHITE
)
def draw_hp(surface, x, y, percentage):
    BAR_LENGHT = 100
    BAR_HEIGHT = 10
    fill = (percentage / 100) * BAR_LENGHT
    borde = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surface, GREEN, fill)
    pygame.draw.rect(surface, WHITE, borde, 4)