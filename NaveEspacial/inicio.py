import pygame

# Configuración
ANCHO = 1024
ALTO = 720
FPS = 60


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

# Ciclo de vida
ejecutando = True
while ejecutando:
    clock.tick(FPS)
    pantalla.blit(fondo, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    pygame.display.flip()
