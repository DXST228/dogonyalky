from pygame import *
from pygame.math import Vector2
from gamesprite import *
from const import *
class Player(Gamesprite):
    def __init__(self, img, x, y, size, speed =5):
        super().__init__(img, x, y, size)
        self.speed = speed
        self.v = Vector2(0,0)
        self.acc = Vector2(0,0)
        self.pos = Vector2(x,y)
    def update(self, up=K_w, down=K_s, left=K_a, right=K_d):
        print(self.pos,self.rect)
        keys = key.get_pressed()
        if keys[up] and self.rect.y>0 :
            self.acc.y-=GAZAN
        if keys[down] and self.rect.bottom<WIN_H :
            self.acc.y+=GAZAN
        if keys[left] and self.rect.x>0 :
            self.acc.x-=GAZAN
        if keys[right] and self.rect.right<WIN_W :
            self.acc.x+=GAZAN
        if 0 > self.rect.x or self.rect.right > WIN_W:
            self.rect.x *= -1
        if 0 > self.rect.y or self.rect.bottom > WIN_H:
            self.rect.y *= -1
        if not any(keys):
            self.v = Vector2(0,0)
            self.acc = Vector2(0,0)
        else:
            self.v+=self.acc
        if self.v.length()>=GAZAN*10:
            self.v.scale_to_length(GAZAN*10)
        self.pos+=self.v
        self.rect.x=self.pos.x
        self.rect.y=self.pos.y
    def update(self, up=K_w, down=K_s, left=K_a, right=K_d):
        keys = key.get_pressed()
        if keys[up] and self.rect.y>0 :
            self.acc.y= -GAZAN
        if keys[down] and self.rect.bottom<WIN_H :
            self.acc.y=GAZAN
        if keys[left] and self.rect.x>0 :
            self.acc.x= -GAZAN
        if keys[right] and self.rect.right<WIN_W :
            self.acc.x=GAZAN
        self.rect.x += self.acc.x
        self.rect.y += self.acc.y