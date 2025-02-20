import pygame

# Configuración
ANCHO = 1024
ALTO = 720
FPS = 60


# Clase de nave
class player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("assets/sprites/nave.png")
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO / 2, ALTO - 50)


# Clase de inicio
class inicio:
    pygame.init()


# Dibujamos la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
fondo = pygame.transform.scale(
    pygame.image.load("assets/fondos/espacio.jpg").convert(), (ANCHO, ALTO)
)
pygame.display.set_caption("Navecilla")

# Establecer FPS
clock = pygame.time.Clock()

# Sprites
Jugador = pygame.sprite.Group()
nave = player()
Jugador.add(nave)

# Ciclo de vida
ejecutando = True
while ejecutando:
    clock.tick(FPS)
    pantalla.blit(fondo, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
    Jugador.draw(pantalla)
    pygame.display.flip()
