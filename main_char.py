import pygame
from pygame.transform import scale
pygame.init()




class mainChar(pygame.sprite.Sprite):
    # конструктор - функция, в которую мы передаем начальные координаты
    def __init__(self, x, y):
        # инициализируем спрайт
        pygame.sprite.Sprite.__init__(self)

        self.HitX = 0
        self.HitY = 25

        # выбираем прямоугольную область размера 50 на 100
        self.rect = pygame.Rect(x, y, 110, 60)

        # загружаем картинку с анимкой st
        self.image1 = []
        self.image1.append(scale(pygame.image.load("templates/sv-st.png"), (115, 110)))
        self.image1.append(scale(pygame.image.load("templates/sv-st2.png"), (115, 110)))



        # загружаем картинку с анимкой l
        self.animation_l = []
        self.animation_l.append(scale(pygame.image.load("templates/sv-l1.png"), (115, 110)))
        self.animation_l.append(scale(pygame.image.load("templates/sv-l2.png"), (115, 110)))



        # загружаем картинку с анимкой up
        self.animation_up = []
        self.animation_up.append(scale(pygame.image.load("templates/sv-r1.png"), (115, 110)))
        self.animation_up.append(scale(pygame.image.load("templates/sv-r2.png"), (115, 110)))



        # загружаем картинку с анимкой r
        self.animation_r = []
        self.animation_r.append(scale(pygame.image.load("templates/sv-r1.png"), (115, 110)))
        self.animation_r.append(scale(pygame.image.load("templates/sv-r2.png"), (115, 110)))



        # загружаем картинку с анимкой down
        self.animation_down = []
        self.animation_down.append(scale(pygame.image.load("templates/sv-r1.png"), (115, 110)))
        self.animation_down.append(scale(pygame.image.load("templates/sv-r2.png"), (115, 110)))



        # задаем начальную скорость по оси x
        self.xvel = 0

        self.frame_l = 0
        self.frame_up = 0
        self.frame_r = 0
        self.frame_down = 0
        self.speed = 10

    # функция перемещения, параметры - нажата ли стрелочки влево и вправо
    def update(self, left, right, up, down, screen, animation_st, debug, run):
        print(self.rect.x, self.rect.y)

        if not (up or down):
            self.yvel = 0

        if ((up and down) and (not right and not left)) or (up and down and left and right):
            self.yvel = 0
            a = int(animation_st)
            screen.blit(self.image1[a], (self.rect.x - self.HitX, self.rect.y - self.HitY))
            return()

        if not (left or right):
            self.xvel = 0

        if (left and right) and (not up and not down):
            self.xvel = 0
            a = int(animation_st)
            screen.blit(self.image1[a], (self.rect.x - self.HitX, self.rect.y - self.HitY))

        # если нажата клавиша влево, уменьшаем скорость

        if left and not right:
            self.frame_l += 0.2
            if (self.frame_l >= 2):
                self.frame_l = 0
            l = int(self.frame_l)
            screen.blit(self.animation_l[l], (self.rect.x - self.HitX, self.rect.y - self.HitY))
            self.xvel = -self.speed


        if right and not left:
            self.xvel = self.speed
            self.frame_r += 0.2
            if (self.frame_r >= 2):
                self.frame_r = 0
            w = int(self.frame_r)
            screen.blit(self.animation_r[w], (self.rect.x - self.HitX, self.rect.y - self.HitY))

        if not (left or right):
            self.xvel = 0

        if (up and not down and not left and not right) or (up and left and right):

            self.frame_up += 0.1
            if (self.frame_up >= 2):
                self.frame_up = 0
            q = int(self.frame_up)
            screen.blit(self.animation_up[q], (self.rect.x - self.HitX, self.rect.y - self.HitY))

        if up and not down:
            self.yvel = -self.speed

        if (down and not up and not left and not right) or (down and left and right):

            self.frame_down += 0.1
            if (self.frame_down >= 2):
                self.frame_down = 0
            e = int(self.frame_down)
            screen.blit(self.animation_down[e], (self.rect.x - self.HitX, self.rect.y - self.HitY))

        if down and not up:
            self.yvel = self.speed

        if not (up or down):
            self.yvel = 0

        if (up and down):
            self.yvel = 0

        if (not (up or down or left or right)):
            a = int(animation_st)
            screen.blit(self.image1[a], (self.rect.x - self.HitX, self.rect.y - self.HitY))


        # изменяем координаты на скорость
        self.rect.x += self.xvel
        self.rect.y += self.yvel


        if debug:
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 4)
            pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)

    def fallback(self):
        self.rect.x -= self.xvel
        self.rect.y -= self.yvel

    def ch_move(self, moveX, moveY):
        self.rect.x += moveX
        self.rect.y += moveY

    def move_(self, x, y):
        self.rect.x = x
        self.rect.y = y