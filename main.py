# pylint: disable=E1101
import pygame
from assets.AssetsManager import AssetsManager
from assets import colors

pygame.init()
ancho_p = 1200
alto_p = 600

assets = AssetsManager(ancho_p, alto_p, 'Dijkstra')
clock = pygame.time.Clock()

def salir_juego():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def main_loop():
    while True:
        salir_juego()
        
        pygame.display.update()
        clock.tick(15)

main_loop()

