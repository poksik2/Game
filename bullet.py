from traceback import print_tb

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.bullet_settings = game.bullet_setting
        self.image = pygame.image.load('images/bullet_up.png')
        self.rect = self.image.get_rect()

        self.moving_up = game.player.moving_up
        self.moving_down = game.player.moving_down
        self.moving_left = game.player.moving_left
        self.moving_right = game.player.moving_right
        self.rect.midtop = game.player.rect.midtop
        self.direction = game.player.direction
        self.x = self.rect.x
        self.y = self.rect.y
        #self.rect = pygame.Rect(self.x, self.y, self.settings.size_w, self.settings.size_h)

    def direct(self):
        pass



    def update(self):
        self.direct()
        if self.direction == 'up':
            self.image = pygame.image.load('images/bullet_up.png')
            self.y -= self.bullet_settings.speed_bullet
        elif self.direction == 'down':
            self.image = pygame.image.load('images/bullet_down.png')
            self.y += self.bullet_settings.speed_bullet
        elif self.direction == 'left':
            self.image = pygame.image.load('images/bullet_left.png')
            self.x -= self.bullet_settings.speed_bullet
        elif self.direction == 'right':
            self.image = pygame.image.load('images/bullet_right.png')
            self.x += self.bullet_settings.speed_bullet
        self.rect.x = self.x
        self.rect.y = self.y


    def draw(self):
        self.screen.blit(self.image,self.rect)

