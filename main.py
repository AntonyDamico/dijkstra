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

def talk(arg):
    print(arg)

def mostrar_sidebar():
    rect_args_list = [ancho_p*0.85, 0, ancho_p*0.15, alto_p]
    rect_args_dic = {'color': colors.AZUL}

    line_args_list = [ancho_p*0.87, alto_p*0.25, ancho_p*0.97, alto_p*0.35]
    line_args_dic = {'w': 10, 'inactive_color':colors.NEGRO, 'active_color': colors.ROJO, 'action': talk, 'args':['hello']}

    circle_args_list = [ancho_p*0.92, alto_p*0.55, 15]
    circle_args_dic = {'inactive_color':colors.NEGRO, 'active_color':colors.ROJO, 'action':talk, 'args':['hello']}

    assets.draw_rect(*rect_args_list, **rect_args_dic)
    assets.draw_line(*line_args_list, **line_args_dic)
    assets.draw_circle(*circle_args_list, **circle_args_dic)




def main_loop():
    while True:
        salir_juego()
        mostrar_sidebar()
        pygame.display.update()
        clock.tick(15)

main_loop()

