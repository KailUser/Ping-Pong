# импорт нужных библиотек и модулей
from pygame import *
from random import randint
from time import time as tm
# фоновая музыка
# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# fire_sound = mixer.Sound('fire.ogg')
# шрифты и надписи
font.init()
font1 = font.Font(None, 80)
win = font1.render('ПОБЕДА! :-)',True,(0,255,0))
lose = font1.render('ПРОИГРЫШ :-(',True,(255,0,0))
font2 = font.Font(None, 36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

# класс главного игрока
class Player(GameSprite):
    def update_pl1(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-85:
            self.rect.x += self.speed
            
    def update_pl2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_width-85:
            self.rect.x += self.speed

# Создаем окошко
win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))