import pygame

# Configuración
ANCHO = 1024
ALTO = 720
FPS = 60


# Clase de nave
class player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("assets/sprites/nave.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO / 2, ALTO - 50)
        self.velocidad_x = 0
        self.velocidad_y = 0

    def update(self):
        self.velocidad_x = 0
        self.velocidad_y = 0

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
            self.velocidad_y = -10
        if teclas[pygame.K_a]:
            self.velocidad_x = -10
        if teclas[pygame.K_s]:
            self.velocidad_y = 10
        if teclas[pygame.K_d]:
            self.velocidad_x = 10

        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > ANCHO - self.rect.width:
            self.rect.x = ANCHO - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > ALTO - self.rect.height:
            self.rect.y = ALTO - self.rect.height


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
    Jugador.update()
    Jugador.draw(pantalla)
    pygame.display.flip()
