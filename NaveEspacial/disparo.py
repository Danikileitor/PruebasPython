import pygame
from inicio import ANCHO_BASE
from inicio import ALTO_BASE
from color import Color


class Disparo(pygame.sprite.Sprite):
    def __init__(self, *groups, x, y):
        super().__init__(*groups)
        self.image = pygame.image.load("assets/sprites/disparo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill
