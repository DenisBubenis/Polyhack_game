import pygame
from pygame.transform import scale
import main_char
#import walls
import mainScene
import cameraMovement
import Data
import logo
import house

print("カマズに殴られた")

pygame.init()
clock = pygame.time.Clock()



cam_X = 0
cam_Y = 0

cam_l = 1
cam_r = 1
cam_up = 1
cam_down = 1

#звук
#run = pygame.mixer.Sound("sounds/бег.wav")
#s = pygame.mixer.Sound("sounds/oan1.wav")
bang = pygame.mixer.Sound("sounds/выстрел.wav")
fon = pygame.mixer.Sound("sounds/фон.wav")
fon2 = pygame.mixer.Sound("sounds/фон2.wav")
lamp = pygame.mixer.Sound("sounds/лампа.wav")

#узнаем разрешение экрана пользователя
info = pygame.display.Info()
width, height = info.current_w, info.current_h


quality = (width, height)
qualityX = quality[0]
qualityY = quality[1]

animation_st = 0
ani_dop = 0.02
value = 0

#Create a displace surface object
DISPLAYSURF = pygame.display.set_mode(size=quality)

mainLoop = True


camRect_l, camRect_r, camRect_up, camRect_down = cameraMovement.cam_init(qualityX, qualityY)


big_sky = pygame.image.load("scene_1/фон.png")
# масштабируем картинку под размер экрана
sky = scale(big_sky, (qualityX, qualityY))

#иницилизируем спрайты:
logo_1 = logo._LOGO_(qualityX / 2 - 200, qualityY / 2 - 200)

Sanek = main_char.mainChar(qualityX / 2 + 100, qualityY / 2 + 80)

House = mainScene.house(510, 0)

objects = []
objects2 = []


objects.append(mainScene.fence(918 + 400 * 1, 980))
objects.append(mainScene.fence(918 + 400 * 2, 980))
objects.append(mainScene.fence(918 + 400 * 3, 980))
objects.append(mainScene.fence(918 + 400 * 4 - 150, 980))

objects2.append(mainScene.fence(518, 75))
objects2.append(mainScene.fence(918, 75))
objects2.append(mainScene.fence(918 + 400 * 1, 75))
objects2.append(mainScene.fence(918 + 400 * 2, 75))
objects2.append(mainScene.fence(918 + 400 * 3, 75))
objects2.append(mainScene.fence(918 + 400 * 4 - 150, 75))

objects.append(mainScene.tree(1100, 300))
objects.append(mainScene.tree(1300, 900))
objects.append(mainScene.tree(1600, 500))
objects.append(mainScene.tree(1900, 800))
objects.append(mainScene.fence(518, 980))
objects.append(mainScene.fence(918, 980))

fontain = mainScene.font(2160, 200)

flor = house.flor(150, -10)

r = 2750

fence2 = mainScene.fence2(515, 340)
fence3 = mainScene.fence2(r, -110)
fence4 = mainScene.fence2(r, 380)

#road = mainScene.road(3000, 600)

island = []

islandX = Data.islandX
islandY = Data.islandY

BlockGenerateX = Data.BlockGenerateX
BlockGenerateY = Data.BlockGenerateY

size = Data.size

for hor in range(BlockGenerateX):
    for vert in range (BlockGenerateY):
        island.append(mainScene.grassBlock1(qualityX / 2 + size * hor + islandX, qualityY / 2 + size * vert + islandY))

logo = True

#прочее:

an_logo = 0

left = False
right = False
up = False
down = False

debug = False






def house_scene(mainloop, left, right, up, down, animation_st, ani_dop, cam_X, cam_Y, debug):
    house = True
    camSoft = 1
    camSpeed = 10
    while house:
        for e in pygame.event.get():
            # if e.type == pygame.KEYDOWN and e.key == pygame.K_LSHIFT:
            #     run = True
            #
            # if e.type == pygame.KEYUP and e.key == pygame.K_LSHIFT:
            #     run = False

            #условия при нажатии кнопок:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_q and debug and Data.showHitBoxes:
                debug = False

            elif e.type == pygame.KEYDOWN and e.key == pygame.K_q and debug == False and Data.showHitBoxes:
                debug = True

            if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
                left = True
                # s.play()

            if e.type == pygame.KEYUP and e.key == pygame.K_a:
                left = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
                right = True
                # s.play()
                #run.play(-1)

            if e.type == pygame.KEYUP and e.key == pygame.K_d:
                right = False
                #run.stop()

            if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
                up = True
                # s.play()

            if e.type == pygame.KEYUP and e.key == pygame.K_w:
                up = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
                down = True
                # s.play()

            if e.type == pygame.KEYUP and e.key == pygame.K_s:
                down = False

            if e.type == pygame.QUIT:
                house = False


        #анимации:

        animation_st += ani_dop
        if (animation_st >= 1):
            ani_dop = 0.02
            if (animation_st >= 2):
                ani_dop = 0.02
                animation_st = 0

        #апдейты (отрисовка):

        DISPLAYSURF.fill((0, 0, 0))

        flor.update(DISPLAYSURF, debug)
        flor.ch_move(cam_X, cam_Y)

        Sanek.update(left, right, up, down, DISPLAYSURF, animation_st, debug, False)
        Sanek.ch_move(cam_X, cam_Y)



        # Debug:
        if debug:
            cameraMovement.debug_draw_camRect(DISPLAYSURF)

        # камера:

        if pygame.Rect.colliderect(Sanek.rect, camRect_l):
            cam_X += camSoft * cam_l
        if not pygame.Rect.colliderect(Sanek.rect, camRect_r) and not pygame.Rect.colliderect(Sanek.rect, camRect_l):
            cam_X = 0

        if (cam_X > camSpeed - 0.1):
            cam_l = 0
        if (cam_X == 0):
            cam_l = 1

        if pygame.Rect.colliderect(Sanek.rect, camRect_r):
            cam_X -= camSoft * cam_r
        if not pygame.Rect.colliderect(Sanek.rect, camRect_r) and not pygame.Rect.colliderect(Sanek.rect, camRect_l):
            cam_X = 0

        if (cam_X < -camSpeed + 0.1):
            cam_r = 0
        if (cam_X == 0):
            cam_r = 1

        if pygame.Rect.colliderect(Sanek.rect, camRect_up):
            cam_Y += camSoft * cam_up
        if not pygame.Rect.colliderect(Sanek.rect, camRect_up) and not pygame.Rect.colliderect(Sanek.rect,
                                                                                               camRect_down):
            cam_Y = 0

        if (cam_Y > camSpeed - 0.1):
            cam_up = 0
        if (cam_Y == 0):
            cam_up = 1

        if pygame.Rect.colliderect(Sanek.rect, camRect_down):
            cam_Y -= camSoft * cam_down
        if not pygame.Rect.colliderect(Sanek.rect, camRect_up) and not pygame.Rect.colliderect(Sanek.rect,
                                                                                               camRect_down):
            cam_Y = 0

        if (cam_Y < -camSpeed + 0.1):
            cam_down = 0
        if (cam_Y == 0):
            cam_down = 1


        if pygame.Rect.colliderect(flor.rect_waalUp, Sanek.rect) or pygame.Rect.colliderect(flor.rect_waalR, Sanek.rect) or pygame.Rect.colliderect(flor.rect_waalL1, Sanek.rect) or pygame.Rect.colliderect(flor.rect_waalL2, Sanek.rect) or pygame.Rect.colliderect(flor.rect_waalDown, Sanek.rect) or pygame.Rect.colliderect(flor.rect_TU, Sanek.rect):
            Sanek.fallback()


        if pygame.Rect.colliderect(flor.rect_exit, Sanek.rect):
            house = False
            main_scene(mainLoop, left, right, up, down, animation_st, ani_dop, cam_X, cam_Y, debug)



        pygame.display.update()

        clock.tick(Data.fps)

def main_scene(mainLoop, left, right, up, down, animation_st, ani_dop, cam_X, cam_Y, debug):
    pygame.font.init()
    #font = pygame.font.SysFont('Comic Sans MS', 30)
    #textsurface = font.render("E - взаимодействовать", False, (255, 255, 255))
    run = False
    camSoft = 1
    camSpeed = 10
    while mainLoop:
        for e in pygame.event.get():
            # if e.type == pygame.KEYDOWN and e.key == pygame.K_LSHIFT:
            #     run = True
            #
            # if e.type == pygame.KEYUP and e.key == pygame.K_LSHIFT:
            #     run = False

            #условия при нажатии кнопок:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_q and debug and Data.showHitBoxes:
                debug = False

            elif e.type == pygame.KEYDOWN and e.key == pygame.K_q and debug == False and Data.showHitBoxes:
                debug = True

            if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
                left = True
                # s.play()

            if e.type == pygame.KEYUP and e.key == pygame.K_a:
                left = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
                right = True
                # s.play()
                #run.play(-1)

            if e.type == pygame.KEYUP and e.key == pygame.K_d:
                right = False
                #run.stop()

            if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
                up = True
                # s.play()

            if e.type == pygame.KEYUP and e.key == pygame.K_w:
                up = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
                down = True
                # s.play()

            if e.type == pygame.KEYUP and e.key == pygame.K_s:
                down = False

            if e.type == pygame.QUIT:
                mainLoop = False

        #анимации:

        animation_st += ani_dop
        if (animation_st >= 1):
            ani_dop = 0.02
            if (animation_st >= 2):
                ani_dop = 0.02
                animation_st = 0

        #апдейты (отрисовка):

        DISPLAYSURF.fill((0, 0, 0))

        DISPLAYSURF.blit(sky, (0, 0))

        #земля:

        for i in island:
            i.update(DISPLAYSURF, debug)

        for t in objects2:
            t.update(DISPLAYSURF, debug)

        House.update(DISPLAYSURF, debug)

        Sanek.update(left, right, up, down, DISPLAYSURF, animation_st, debug, run)


        fontain.update(DISPLAYSURF, debug)

        fence2.update(DISPLAYSURF, debug)
        fence3.update(DISPLAYSURF, debug)
        fence4.update(DISPLAYSURF, debug)

        #road.update(DISPLAYSURF, debug)

        for q in objects:
            q.update(DISPLAYSURF, debug)



        #DISPLAYSURF.blit(textsurface, (20, 20))

        #tree.update(DISPLAYSURF, debug)
        #tree2.update(DISPLAYSURF, debug)


        #Debug:
        if debug:
            cameraMovement.debug_draw_camRect(DISPLAYSURF)

        #камера:


        if pygame.Rect.colliderect(Sanek.rect, camRect_l):
            cam_X += camSoft * cam_l
        if not pygame.Rect.colliderect(Sanek.rect, camRect_r) and not pygame.Rect.colliderect(Sanek.rect, camRect_l):
            cam_X = 0

        if (cam_X > camSpeed - 0.1):
            cam_l = 0
        if (cam_X == 0):
            cam_l = 1

        if pygame.Rect.colliderect(Sanek.rect, camRect_r):
            cam_X -= camSoft * cam_r
        if not pygame.Rect.colliderect(Sanek.rect, camRect_r) and not pygame.Rect.colliderect(Sanek.rect, camRect_l):
            cam_X = 0

        if (cam_X < -camSpeed + 0.1):
            cam_r = 0
        if (cam_X == 0):
            cam_r = 1



        if pygame.Rect.colliderect(Sanek.rect, camRect_up):
            cam_Y += camSoft * cam_up
        if not pygame.Rect.colliderect(Sanek.rect, camRect_up) and not pygame.Rect.colliderect(Sanek.rect, camRect_down):
            cam_Y = 0

        if (cam_Y > camSpeed - 0.1):
            cam_up = 0
        if (cam_Y == 0):
            cam_up = 1

        if pygame.Rect.colliderect(Sanek.rect, camRect_down):
            cam_Y -= camSoft * cam_down
        if not pygame.Rect.colliderect(Sanek.rect, camRect_up) and not pygame.Rect.colliderect(Sanek.rect, camRect_down):
            cam_Y = 0

        if (cam_Y < -camSpeed + 0.1):
            cam_down = 0
        if (cam_Y == 0):
            cam_down = 1


        Sanek.ch_move(cam_X, cam_Y)
        House.ch_move(cam_X, cam_Y)
        fontain.ch_move(cam_X, cam_Y)
        fence2.ch_move(cam_X, cam_Y)
        fence3.ch_move(cam_X, cam_Y)
        fence4.ch_move(cam_X, cam_Y)

        for w in objects:
            w.ch_move(cam_X, cam_Y)

        for i in objects2:
            i.ch_move(cam_X, cam_Y)





        for i in island:
            i.ch_move(cam_X, cam_Y)


        #физика:

        if pygame.Rect.colliderect(House.rect, Sanek.rect) or pygame.Rect.colliderect(fontain.rect, Sanek.rect) or pygame.Rect.colliderect(House.rect2, Sanek.rect) or pygame.Rect.colliderect(fence2.rect, Sanek.rect) or pygame.Rect.colliderect(fence3.rect, Sanek.rect) or pygame.Rect.colliderect(fence4.rect, Sanek.rect):
            Sanek.fallback()

        for e in objects:
            if pygame.Rect.colliderect(e.rect, Sanek.rect):
                Sanek.fallback()

        for u in objects2:
            if pygame.Rect.colliderect(u.rect, Sanek.rect):
                Sanek.fallback()

        if pygame.Rect.colliderect(House.enter_rect, Sanek.rect):
            mainLoop = False
            fon.stop()
            fon2.play(-1)
            house_scene(mainLoop, left, right, up, down, animation_st, ani_dop, cam_X, cam_Y, debug)




        #всегда последнее (обновление холста)

        pygame.display.update()

        clock.tick(Data.fps)

def LOGO(logo, an_logo, bang, mainLoop, left, right, up, down, animation_st, ani_dop, cam_X, cam_Y, debug):
    go = False
    while logo:

        for e in pygame.event.get():


            #условия при нажатии кнопок:


            if e.type == pygame.QUIT:
                logo = False
        if go:
            logo = False
            main_scene(mainLoop, left, right, up, down, animation_st, ani_dop, cam_X, cam_Y, debug)


        DISPLAYSURF.fill((0, 0, 0))

        if (an_logo > 60 and an_logo < 180 or an_logo > 182 and an_logo < 184 or an_logo > 186 and an_logo < 187):
            logo_1.update(DISPLAYSURF)

        if (an_logo == 60):
            lamp.play()
            #bang.play()

        if (an_logo == 250):
            fon.play(-1)

        if (an_logo == 270):
            go = True



        an_logo += 1

        pygame.display.update()

        clock.tick(60)



LOGO(logo, an_logo, bang, mainLoop, left, right, up, down, animation_st, ani_dop, cam_X, cam_Y, debug)

#main_scene(mainLoop, left, right, up, down, animation_st, ani_dop, cam_X, cam_Y, debug)


pygame.quit()