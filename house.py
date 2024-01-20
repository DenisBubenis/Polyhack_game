import pygame
from pygame.transform import scale

pygame.init()

class flor(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.size = 900

        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.rect_exit = pygame.Rect(x + 891, y + 515, 20, 80)
        self.rect_waalUp = pygame.Rect(x, y, 900, 180)
        self.rect_waalR = pygame.Rect(x + 900, y, 20, 900)
        self.rect_waalL1 = pygame.Rect(x, y, 20, 300)
        self.rect_waalL2 = pygame.Rect(x, y + 500, 20, 400)
        self.rect_waalDown = pygame.Rect(x, y + 895, 900, 20)
        self.rect_TU = pygame.Rect(x, y + 730, 280, 250)
        self.rect_Dor = pygame.Rect(x + 754, y, 280, 400)

        self.img = scale(pygame.image.load("Houe/КОМНАТА1.png"), (self.size, self.size))

        self.xvel = 0
        self.yvel = 0

    def update(self, screen, debug):
        screen.blit(self.img, (self.rect.x, self.rect.y))
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        self.rect_exit.x += self.xvel
        self.rect_exit.y += self.yvel
        self.rect_waalUp.x += self.xvel
        self.rect_waalUp.y += self.yvel
        self.rect_waalR.x += self.xvel
        self.rect_waalR.y += self.yvel
        self.rect_waalL1.x += self.xvel
        self.rect_waalL1.y += self.yvel
        self.rect_waalL2.x += self.xvel
        self.rect_waalL2.y += self.yvel
        self.rect_waalDown.x += self.xvel
        self.rect_waalDown.y += self.yvel
        self.rect_TU.x += self.xvel
        self.rect_TU.y += self.yvel
        self.rect_Dor.x += self.xvel
        self.rect_Dor.y += self.yvel

        if debug:
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 3)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
            pygame.draw.rect(screen, (255, 0, 0), self.rect_exit, 3)
            pygame.draw.rect(screen, (0, 0, 0), self.rect_exit, 2)
            pygame.draw.rect(screen, (255, 0, 255), self.rect_waalUp, 3)
            pygame.draw.rect(screen, (255, 0, 0), self.rect_waalUp, 2)
            pygame.draw.rect(screen, (255, 0, 255), self.rect_waalR, 3)
            pygame.draw.rect(screen, (255, 0, 0), self.rect_waalR, 2)
            pygame.draw.rect(screen, (255, 0, 255), self.rect_waalL1, 3)
            pygame.draw.rect(screen, (255, 0, 0), self.rect_waalL1, 2)
            pygame.draw.rect(screen, (255, 0, 255), self.rect_waalL2, 3)
            pygame.draw.rect(screen, (255, 0, 0), self.rect_waalL2, 2)
            pygame.draw.rect(screen, (255, 0, 255), self.rect_waalDown, 3)
            pygame.draw.rect(screen, (255, 0, 0), self.rect_waalDown, 2)
            pygame.draw.rect(screen, (255, 0, 255), self.rect_TU, 3)
            pygame.draw.rect(screen, (255, 0, 0), self.rect_TU, 2)
            pygame.draw.rect(screen, (255, 0, 255), self.rect_Dor, 3)
            pygame.draw.rect(screen, (255, 0, 0), self.rect_Dor, 2)

    def ch_move(self, moveX, moveY):
        self.rect.x += moveX
        self.rect.y += moveY
        self.rect_exit.x += moveX
        self.rect_exit.y += moveY
        self.rect_waalUp.x += moveX
        self.rect_waalUp.y += moveY
        self.rect_waalR.x += moveX
        self.rect_waalR.y += moveY
        self.rect_waalL1.x += moveX
        self.rect_waalL1.y += moveY
        self.rect_waalL2.x += moveX
        self.rect_waalL2.y += moveY
        self.rect_waalDown.x += moveX
        self.rect_waalDown.y += moveY
        self.rect_TU.x += moveX
        self.rect_TU.y += moveY
        self.rect_Dor.x += moveX
        self.rect_Dor.y += moveY

class coridor(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        scale1 = 6


        self.rect = pygame.Rect(x, y, 192 * scale1, 101 * scale1)

        self.rect2 = pygame.Rect(x, y + 220, 192 * scale1, 101 * scale1 - 280)


        self.img = scale(pygame.image.load("Houe/коридор1.jpg"), (192 * scale1, 101 * scale1))

        self.xvel = 0
        self.yvel = 0
    def update(self, screen, debug):
        screen.blit(self.img, (self.rect.x, self.rect.y))

        self.rect.x += self.xvel
        self.rect.y += self.yvel
        self.rect2.x += self.xvel
        self.rect2.y += self.yvel

        if debug:
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 3)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
            pygame.draw.rect(screen, (0, 255, 255), self.rect2, 3)
            pygame.draw.rect(screen, (0, 0, 0), self.rect2, 2)

    def ch_move(self, moveX, moveY):
        self.rect.x += moveX
        self.rect.y += moveY
        self.rect2.x += moveX
        self.rect2.y += moveY

class down_room(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        scale1 = 1300


        self.rect = pygame.Rect(x, y, 1 * scale1, 1 * scale1)

        self.rect2 = pygame.Rect(x, y, 1 * scale1, 1 * scale1)


        self.img = scale(pygame.image.load("Houe/КОМНАТА2.png"), (1 * scale1, 1 * scale1))

        self.xvel = 0
        self.yvel = 0
    def update(self, screen, debug):
        screen.blit(self.img, (self.rect.x, self.rect.y))

        self.rect.x += self.xvel
        self.rect.y += self.yvel
        self.rect2.x += self.xvel
        self.rect2.y += self.yvel

        if debug:
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 3)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
            pygame.draw.rect(screen, (0, 255, 255), self.rect2, 3)
            pygame.draw.rect(screen, (0, 0, 0), self.rect2, 2)

    def ch_move(self, moveX, moveY):
        self.rect.x += moveX
        self.rect.y += moveY
        self.rect2.x += moveX
        self.rect2.y += moveY