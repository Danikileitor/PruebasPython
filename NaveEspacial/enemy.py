import pygame

ANCHO_BASE = 1024
ALTO_BASE = 720

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
H_FA2F2F = (250, 47, 47)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)


class enemy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("assets/sprites/ovni.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO_BASE / 2, 50)
        self.velocidad_x = 0
        self.velocidad_y = 0
