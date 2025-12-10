import pygame
from circulo1 import Circulo1
from circulo2 import Circulo2 

pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Colision circular en Pygame")

backround = (0, 0, 0)
color_colision = (234, 63, 63)

circulo1 = Circulo1(200, 200, 100, 50)
circulo2 = Circulo2(400, 300, 150, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    teclas = pygame.key.get_pressed()
    
    pos_anterior_1 = circulo1.obtener_posicion
    pos_anterior_2 = circulo2.obtener_posicion

    circulo1.mover(teclas)
    circulo2.mover(teclas)

    if circulo1.rect.colliderect(circulo2.rect):
        circulo1.restablecer_posicion(*pos_anterior_1)
        circulo2.restablecer_posicion(*pos_anterior_2)
        circulo1.cambiar_color((63, 232, 234), color_colision)
        circulo2.cambiar_color((63, 234, 76), color_colision)
    else:
        circulo1.cambiar_color((63, 232, 234))
        circulo2.cambiar_color((63, 234, 76))

    ventana.fill(backround)
    circulo1.dibujar(ventana)
    circulo2.dibujar(ventana)

    pygame.display.update()

pygame.quit()

    