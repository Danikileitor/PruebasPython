import pygame
from enemy import Enemy
from disparo import Disparo

# Configuración
ANCHO_BASE = 1024
ALTO_BASE = 720
FPS = 60
pantalla = pygame.display.set_mode((ANCHO_BASE, ALTO_BASE))
ventana = pygame.display.Info()
ANCHO = ventana.current_w
ALTO = ventana.current_h


# Clase de nave
class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("assets/sprites/nave.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO / 2, ALTO - 50)
        self.velocidad = 5
        self.velocidad_x = 0
        self.velocidad_y = 0

    def update(self):
        self.velocidad_x = 0
        self.velocidad_y = 0

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.velocidad_y = -self.velocidad
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.velocidad_x = -self.velocidad
        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.velocidad_y = self.velocidad
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.velocidad_x = self.velocidad
        if teclas[pygame.K_SPACE]:
            self.disparar()

        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

    def disparar(self):
        disparo = Disparo(x=self.rect.centerx, y=self.rect.top)
        Disparos.add(disparo)


# Clase de inicio
class inicio:
    pygame.init()


# Dibujamos la pantalla
fondo = pygame.transform.scale(
    pygame.image.load("assets/fondos/espacio.jpg").convert(),
    (ANCHO, ALTO),
)
pygame.display.set_caption("Navecilla")

# Establecer FPS
clock = pygame.time.Clock()

# Sprites
Jugador = pygame.sprite.Group()
nave = Player()
Jugador.add(nave)
Disparos = pygame.sprite.Group()
Enemigos = pygame.sprite.Group()

# Ciclo de vida
ejecutando = True
while ejecutando:
    clock.tick(FPS)
    if pygame.WINDOWSIZECHANGED:
        ventana = pygame.display.Info()
        ANCHO = ventana.current_w
        ALTO = ventana.current_h
        fondo = pygame.transform.scale(
            pygame.image.load("assets/fondos/espacio.jpg").convert(),
            (ANCHO, ALTO),
        )
    pantalla.blit(fondo, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
    Jugador.update()
    Enemigos.update()
    Disparos.update()

    if not Enemigos:
        for x in range(5):
            ovni = Enemy(ANCHO=ANCHO, ALTO=ALTO)
            Enemigos.add(ovni)

    Jugador.draw(pantalla)
    Enemigos.draw(pantalla)
    Disparos.draw(pantalla)
    pygame.display.flip()
