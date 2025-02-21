import pygame
import random
from inicio import ANCHO_BASE
from inicio import ALTO_BASE
from color import Color


class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups, ANCHO, ALTO):
        super().__init__(*groups)
        self.ANCHO = ANCHO
        self.ALTO = ALTO
        self.image = pygame.image.load("assets/sprites/ovni.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO / 2, ALTO / 4 / 2)
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(int(ALTO / 4) - self.rect.height)
        self.velocidad_x = 0
        self.velocidad_y = 1

    def update(self):
        self.velocidad_x = random.randint(-20, 20)
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.ANCHO:
            self.rect.right = self.ANCHO
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.ALTO:
            self.rect.bottom = self.ALTO
