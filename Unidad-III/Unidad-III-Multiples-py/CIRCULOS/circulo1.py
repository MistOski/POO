import pygame
class Circulo1:
    def __init__(self, x, y, radio, color=(255, 0, 0), velocidad=5):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.velocidad = velocidad
    def dibujar(self, ventana):
        pygame.draw.circle(ventana, self.color, (int(self.x), int(self.y)), self.radio)
    def mover(self, teclas):
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
    def obtener_posicion(self):
        return self.x, self.y
    def restablecer_posicion(self, x, y):
        self.x = x
        self.y = y
    def cambiar_color(self, color):
        self.color = color