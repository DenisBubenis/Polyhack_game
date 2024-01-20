import pygame
import random
import Data
from pygame.transform import scale
pygame.init()

class grassBlock1(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.size = Data.size

        self.rect = pygame.Rect(x, y, self.size, self.size)

        self.img = scale(pygame.image.load("scene_1/кусокЛандшафтаНомер1.jpg"), (self.size, self.size))
        self.img2 = scale(pygame.image.load("scene_1/кусокЛандшафтаНомер2.jpg"), (self.size, self.size))
        self.img3 = scale(pygame.image.load("scene_1/кусокЛандшафтаНомер3.jpg"), (self.size, self.size))
        self.img4 = scale(pygame.image.load("scene_1/Монтажная область 2.jpg"), (self.size, self.size))
        self.img5 = scale(pygame.image.load("scene_1/Монтажная область 2-1.jpg"), (self.size, self.size))
        self.img6 = scale(pygame.image.load("scene_1/Монтажная область 2-2.jpg"), (self.size, self.size))

        variants = [self.img, self.img2, self.img3, self.img4, self.img5, self.img6]

        self.island = random.choice(variants)

        self.xvel = 0
        self.yvel = 0

    def update(self, screen, debug):

        screen.blit(self.island, (self.rect.x, self.rect.y))
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if debug:
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 3)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

    def ch_move(self, moveX, moveY):
        self.rect.x += moveX
        self.rect.y += moveY

class house(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        size = 800

        hitBoxX_size = 180
        hitBoxY_size = 450

        hitBoxX_size2 = 140
        hitBoxY_size2 = 5

        hitBoxX_size3 = 160
        hitBoxY_size3 = 450

        self.HitX = 150
        self.HitY = 300

        self.rect = pygame.Rect(x, y, hitBoxX_size, hitBoxY_size)

        self.enter_rect = pygame.Rect(x + 188, y + 400, hitBoxX_size2, hitBoxY_size2)

        self.rect2 = pygame.Rect(x + 330, y, hitBoxX_size3, hitBoxY_size3)

        self.img = scale(pygame.image.load("scene_1/testHouse2.png"), (size, size))

        self.xvel = 0
        self.yvel = 0

    def update(self, screen, debug):

        screen.blit(self.img, (self.rect.x - self.HitX, self.rect.y - self.HitY))
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        self.enter_rect.x += self.xvel
        self.enter_rect.y += self.yvel
        self.rect2.x += self.xvel
        self.rect2.y += self.yvel
        if debug:
            pygame.draw.rect(screen, (0, 255, 255), self.rect, 5)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
            pygame.draw.rect(screen, (100, 60, 80), self.enter_rect, 5)
            pygame.draw.rect(screen, (78, 0, 35), self.enter_rect, 2)
            pygame.draw.rect(screen, (255, 255, 80), self.rect2, 5)
            pygame.draw.rect(screen, (0, 255, 0), self.rect2, 2)

    def ch_move(self, moveX, moveY):
        self.rect.x += moveX
        self.rect.y += moveY
        self.enter_rect.x += moveX
        self.enter_rect.y += moveY
        self.rect2.x += moveX
        self.rect2.y += moveY

class tree(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        size = 400

        hitBoxX_size = 160
        hitBoxY_size = 10

        self.HitX = 130
        self.HitY = 350

        self.rect = pygame.Rect(x, y, hitBoxX_size, hitBoxY_size)

        self.img = scale(pygame.image.load("scene_1/tree.png"), (size, size))

        self.xvel = 0
        self.yvel = 0

    def update(self, screen, debug):

        screen.blit(self.img, (self.rect.x - self.HitX, self.rect.y - self.HitY))
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if debug:
            pygame.draw.rect(screen, (0, 255, 255), self.rect, 5)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

    def ch_move(self, moveX, moveY):
        self.rect.x += moveX
        self.rect.y += moveY

class fence(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        size = 400

        hitBoxX_size = 400
        hitBoxY_size = 5

        self.HitX = 0
        self.HitY = 80

        self.rect = pygame.Rect(x, y, hitBoxX_size, hitBoxY_size)

        self.img = scale(pygame.image.load("scene_1/забор.png"), (size, size))

        self.xvel = 0
        self.yvel = 0

    def update(self, screen, debug):

        screen.blit(self.img, (self.rect.x - self.HitX, self.rect.y - self.HitY))
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if debug:
            pygame.draw.rect(screen, (0, 255, 255), self.rect, 5)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

    def ch_move(self, moveX, moveY):
        self.rect.x += moveX
        self.rect.y += moveY

class road(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        size = 300

        hitBoxX_size = 400
        hitBoxY_size = 400

        self.HitX = 0
        self.HitY = 80

        self.rect = pygame.Rect(x, y, hitBoxX_size, hitBoxY_size)

        self.img = scale(pygame.image.load("scene_1/car.png"), (size, size))

        self.xvel = 0
        self.yvel = 0

    def update(self, screen, debug):

        screen.blit(self.img, (self.rect.x - self.HitX, self.rect.y - self.HitY))
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if debug:
            pygame.draw.rect(screen, (0, 255, 255), self.rect, 5)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

    def ch_move(self, moveX, moveY):
        self.rect.x += moveX
        self.rect.y += moveY

class font(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        size = 600

        hitBoxX_size = 600
        hitBoxY_size = 280

        self.HitX = 0
        self.HitY = 180

        self.rect = pygame.Rect(x, y, hitBoxX_size, hitBoxY_size)

        self.img = scale(pygame.image.load("scene_1/фонтан.png"), (size, size))

        self.xvel = 0
        self.yvel = 0

    def update(self, screen, debug):

        screen.blit(self.img, (self.rect.x - self.HitX, self.rect.y - self.HitY))
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if debug:
            pygame.draw.rect(screen, (0, 255, 255), self.rect, 5)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

    def ch_move(self, moveX, moveY):
        self.rect.x += moveX
        self.rect.y += moveY

class fence2(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        size = 600

        hitBoxX_size = 20
        hitBoxY_size = 600

        self.HitX = 270
        self.HitY = 0

        self.rect = pygame.Rect(x, y, hitBoxX_size, hitBoxY_size)

        self.img = scale(pygame.image.load("scene_1/забор2.png"), (size, size))

        self.xvel = 0
        self.yvel = 0

    def update(self, screen, debug):

        screen.blit(self.img, (self.rect.x - self.HitX, self.rect.y - self.HitY))
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if debug:
            pygame.draw.rect(screen, (0, 255, 255), self.rect, 5)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

    def ch_move(self, moveX, moveY):
        self.rect.x += moveX
        self.rect.y += moveY