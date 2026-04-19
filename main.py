from pygame import *
from const import *
from gamesprite import *
from player import *
#from classes import*


def give_birth():
    teodor = Player(PLATFORM,(WIN_W-P_SIZE[0])/2,WIN_H-100, P_SIZE)
    semechk = Player(BALL,(WIN_W-B_SIZE[0])/2,WIN_H-170, B_SIZE)
    return(teodor, semechk)


font.init()
# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота
# создание окна размером 700 на 500
window = display.set_mode((WIN_W, WIN_H))
# создание таймера
clock = time.Clock()

# название окна
display.set_caption("Я грр, ты мне?")

# задать картинку фона такого же размера, как размер окна
background = Gamesprite(FON, 0, 0, (WIN_W,WIN_H))

teodor, semechk = give_birth()

#record =  Card(0, 0, WIN_W, WIN_H )
#record.set_text('Красавчик, но мог быстрее ')
# игровой цикл
game = True
finish = False
while game:
    if not finish:
        # отобразить картинку фона
        background.draw(window)
        teodor.draw(window)
        teodor.drawrect(window)
        teodor.update()
        semechk.draw(window)
        semechk.update(K_UP, K_DOWN, K_LEFT,K_RIGHT)

    #     if sprite.collide_rect(platform, ball):
    #         ball.speed_y *= -1
    #     if sprite.spritecollide( ball,monsters, True):
    #         ball.speed_y *= -1
    # else: 
    #     pass
        #record.draw(window)
        

    # слушать события и обрабатывать
    for e in event.get():
        if e.type == KEYDOWN: 
            if e.key == K_p: 
                if finish: 
                    teodor, semechk = give_birth()
                    finish = False
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()
    clock.tick(FPS)
