import pygame, sys, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size_w = 1024
size_h = 768

class Tank(pygame.sprite.Sprite):
    w_tank = 32
    h_tank = 32
    speed = 5

    def __init__(self, surface, color):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surface
        self.color = color
        self.x = surface.get_width() // 2
        self.y = surface.get_height() // 2

    def move_down(self):
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, self.w_tank, self.h_tank))
        self.y += self.speed
        screen.blit(pygame.image.load("tank_down.png"), (t.x, t.y))
        pygame.display.update()

    def move_up(self):
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, self.w_tank, self.h_tank))
        self.y -= self.speed
        screen.blit(pygame.image.load("tank_up.png"), (t.x, t.y))
        pygame.display.update()

    def move_right(self):
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, self.w_tank, self.h_tank))
        self.x += self.speed
        screen.blit(pygame.image.load("tank_right.png"), (t.x, t.y))
        pygame.display.update()

    def move_left(self):
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, self.w_tank, self.h_tank))
        self.x -= self.speed
        screen.blit(pygame.image.load("tank_left.png"), (t.x, t.y))
        pygame.display.update()


class Field(pygame.sprite.Sprite):

    def border():
        if t.x < 0 or t.x > size_w:
            t.x = 0
        elif t.x > screen.get_width() - 32:
            t.x = screen.get_width() - 32
        if t.y < 0 or t.y > size_h:
            t.y = 0
        elif t.y > screen.get_height() - 32:
            t.y = screen.get_height() - 32


screen = pygame.display.set_mode((size_w, size_h))
f = Field
t = Tank(screen, WHITE)
pygame.init()
pygame.display.flip()
pygame.time.Clock().tick(30)

screen.fill(WHITE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        f.border()

        key = pygame.key.get_pressed()
        #print(key)
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            t.move_down()

        if key[pygame.K_UP] or key[pygame.K_w]:
            t.move_up()

        if key[pygame.K_LEFT] or key[pygame.K_a]:
            t.move_left()

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            t.move_right()
