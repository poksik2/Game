import sys

import pygame
from setting import *
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.player_setting = PlayerSetting()
        self.screen_setting = ScreenSetting()
        self.color_setting = ColorSetting()

        self.screen = pygame.display.set_mode((self.screen_setting.size_w, self.screen_setting.size_h))
        self.clock = pygame.time.Clock()
        self.player = Player(self)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_d:
            self.player.moving_right = True

        elif event.key == pygame.K_a:
            self.player.moving_left = True

        elif event.key == pygame.K_w:
            self.player.moving_up = True

        elif event.key == pygame.K_s:
            self.player.moving_down = True

        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_a:
            self.player.moving_left = False
        elif event.key == pygame.K_w:
            self.player.moving_up = False
        elif event.key == pygame.K_s:
            self.player.moving_down = False

    def update_screen(self):
        self.screen.fill(self.color_setting.WHITE)
        self.player.update_position()
        self.player.update_sprite()
        self.player.draw()
        pygame.display.flip()

    def start(self):
        while True:
            self.clock.tick(60)
            self._check_events()
            self.update_screen()


if __name__ == '__main__':
    game = Game()
    game.start()
