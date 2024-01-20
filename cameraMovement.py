import pygame

def cam_init(x, y):
    global camRect_l, camRect_r, camRect_up, camRect_down
    camRect_l = pygame.Rect(x / 2 - 800, y / 2 - 400, 120, 800)
    camRect_r = pygame.Rect(x / 2 + 680, y / 2 - 400, 120, 800)
    camRect_up = pygame.Rect(x / 2 - 800, y / 2 - 420, 1600, 120)
    camRect_down = pygame.Rect(x / 2 - 800, y / 2 + 320, 1600, 120)
    return camRect_l, camRect_r, camRect_up, camRect_down

def debug_draw_camRect(screen):
    pygame.draw.rect(screen, (0, 0, 0), camRect_l, 4)
    pygame.draw.rect(screen, (0, 0, 0), camRect_r, 4)
    pygame.draw.rect(screen, (0, 0, 0), camRect_up, 4)
    pygame.draw.rect(screen, (0, 0, 0), camRect_down, 4)
    pygame.draw.rect(screen, (255, 255, 0), camRect_l, 2)
    pygame.draw.rect(screen, (255, 255, 0), camRect_r, 2)
    pygame.draw.rect(screen, (255, 255, 0), camRect_up, 2)
    pygame.draw.rect(screen, (255, 255, 0), camRect_down, 2)