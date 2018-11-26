# pylint: disable=E1101
import pygame
from assets.AssetsManager import AssetsManager
from assets import colors

pygame.init()
ancho_p = 1200
alto_p = 600

assets = AssetsManager(ancho_p, alto_p, 'Dijkstra')
clock = pygame.time.Clock()

assets.background_color(colors.NEGRO)

def salir_juego():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def mostrar_sidebar():
    assets.draw_rect(ancho_p*0.85, 0, ancho_p*0.15, alto_p, color=colors.AZUL)
    assets.draw_line(ancho_p*0.87, alto_p*0.25, ancho_p*0.97, alto_p*0.35, w=10)
    assets.draw_circle(ancho_p*0.92, alto_p*0.55, 10)

def main_loop():
    while True:
        salir_juego()
        mostrar_sidebar()
        pygame.display.update()
        clock.tick(15)

main_loop()

