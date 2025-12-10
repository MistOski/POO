import pygame
class Circulo2:
    def __init__(self, x, y, radio, velocidad=1, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.radio = radio
        self.velocidad = velocidad
        self.color = color
    def dibujar(self, ventana):
        pygame.draw.circle(ventana, self.color, (int(self.x), int(self.y)), int(self.radio))
    def mover(self, teclas=None):
        if teclas is None:
            teclas = pygame.key.get_pressed()
        mov_x = 0
        mov_y = 0
        if teclas[pygame.K_a]:
            mov_x -= 1
        if teclas[pygame.K_d]:
            mov_x += 1
        if teclas[pygame.K_w]:
            mov_y -= 1
        if teclas[pygame.K_s]:
            mov_y += 1
        self.x += mov_x * self.velocidad
        self.y += mov_y * self.velocidad
    def restablecer_posicion(self, x, y):
        self.x = x
        self.y = y
    def cambiar_color(self, color):
        self.color = color