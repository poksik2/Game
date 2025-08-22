import pygame





class Player:
    def __init__(self, game):

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.player_setting = game.player_setting

        self.image = pygame.image.load(f'images/tank_down.png')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_sprite(self):
        if self.moving_up:
            self.image = pygame.image.load('images/tank_up.png')
        elif self.moving_down:
            self.image = pygame.image.load('images/tank_down.png')
        elif self.moving_right:
            self.image = pygame.image.load('images/tank_right.png')
        elif self.moving_left:
            self.image = pygame.image.load('images/tank_left.png')

    def update_position(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.player_setting.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.player_setting.speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.player_setting.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.player_setting.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)
