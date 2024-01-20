import pygame
from pygame.transform import scale
import random
pygame.init()

class _LOGO_(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(x, y, 400, 400)

        self.img = scale(pygame.image.load("logo/Logo.png"), (400, 400))
    def update(self, screen):

        screen.blit(self.img, (self.rect.x + random.randint(1, 10), self.rect.y + random.randint(1, 10)))