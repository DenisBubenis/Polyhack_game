import pygame
from pygame.transform import scale

walls = [
    pygame.Rect(100, 100, 200, 200),
    pygame.Rect(500, 700, 400, 200),
]

def debug_draw_walls(screen):
    for wall in walls:
        pygame.draw.rect(screen, (255, 0, 0), wall, 2)