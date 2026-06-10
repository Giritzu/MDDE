#importaciones
import pygame as pg
import os
from archivos_necesarios import main_menu
from archivos_necesarios import botones
from archivos_necesarios import constantes
#pestaña principal
pg.init()
screen = pg.display.set_mode((1280,720))
titulo = pg.display.set_caption("MDDE")
time = pg.time.Clock()
run = True

#codigo principal
while run == True:

    #si le dan a quit para poder salir del juego
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            run = False

    #llamo al menu principal para dibujar la pantalla del menu principal
    menu_principal = main_menu.mainmenu(screen)
    pantalla_principal = menu_principal.draw()

    #botones


    #actualizar la pantalla
    pg.display.update()

    #fps
    time.tick(30)

#cierro por completo el funcionamiento e pygame
pg.quit()
