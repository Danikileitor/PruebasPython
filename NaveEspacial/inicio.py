import pygame

# Dimensiones de ventana
ANCHO = 1024
ALTO = 720


# Clase de inicio
class inicio:
    pygame.init()


# Dibujamos la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Ciclo de vida
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    pygame.display.flip()
