#importaciones
import pygame as pg
import os
from archivos_necesarios import main_menu
from archivos_necesarios import botones
from archivos_necesarios import constantes
from archivos_necesarios import functions

#pestaña principal
pg.init()
screen = pg.display.set_mode((1280,720))
titulo = pg.display.set_caption("MDDE")
time = pg.time.Clock()
run = True

#estado del menu actual
menu_state = "PRINCIPAL_MENU"
#cargamos el main menu
menu_principal = main_menu.mainmenu(screen)
menu_opciones = main_menu.opciones(screen)
#codigo principal
while run == True:

    #si le dan a quit para poder salir del juego
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            run = False
        elif evento.type == pg.MOUSEBUTTONDOWN:
            if evento.button == 1:
                pos_click = evento.pos
                
    #tomamos la posicion del mouse en todo momento
    mouse_position = pg.mouse.get_pos()

    #borramos la pantalla
    screen.fill((0, 0, 0))

    if menu_state == "PRINCIPAL_MENU":
        #dibujamos los botones
        menu_principal.draw()
        #si es que se llegan a tocar los botones
        menu_principal.update_color(mouse_position)


    elif menu_state == "OPTIONS":
        pass


    #actualizar la pantalla
    pg.display.update()

    #fps
    time.tick(30)

#cierro por completo el funcionamiento e pygame
pg.quit()
