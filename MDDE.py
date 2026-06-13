#importaciones
import pygame as pg
import os
from archivos_necesarios import main_menu
from archivos_necesarios import botones
from archivos_necesarios import constantes
from archivos_necesarios import functions
from archivos_necesarios import caja_de_texto
from archivos_necesarios import game

#pestaña principal
pg.init()
screen = pg.display.set_mode((1280,720))
titulo = pg.display.set_caption("MDDE")
time = pg.time.Clock()
run = True

actual_state = "PRINCIPAL_MENU"
#cargamos el main menu
menu_principal = main_menu.mainmenu(screen)
menu_opciones = main_menu.opciones(screen)
#codigo principal
while run == True:

    #este es el bloque de acciones exactas (se ejecutan una sola vez por cada frame)
    for evento in pg.event.get():
        #si se detecta que se le da al boton x de la ventana para poder cerrarlo
        if evento.type == pg.QUIT:
            run = False
        #vemos si se ejecuta algun click
        elif evento.type == pg.MOUSEBUTTONDOWN:
            if evento.button == 1:
                #obtenemos su posicion en el momento preciso donde se hizo click
                pos_click = evento.pos

                #para que no sucedan errores extraños
                if actual_state == "PRINCIPAL_MENU":
                    #guardamos si se hizo algun click con alguna de las opciones
                    opcion_seleccionada = menu_principal.manage_click(pos_click)

                    if opcion_seleccionada == "Options":
                        actual_state = "OPCIONES"

                    if opcion_seleccionada == "Exit":
                        run = False

                #para cuando estamos en el menu de opciones
                if actual_state == "OPCIONES":
                    opcion_seleccionada = menu_opciones.manage_click(pos_click)

                    if opcion_seleccionada == "Exit":
                        actual_state = "PRINCIPAL_MENU"

    #tomamos la posicion del mouse en todo momento
    mouse_position = pg.mouse.get_pos()

    #borramos la pantalla
    screen.fill((0, 0, 0))

    if actual_state == "PRINCIPAL_MENU":
        #dibujamos los botones
        menu_principal.draw()
        #si es que se llegan a tocar los botones
        menu_principal.update_color(mouse_position)


    elif actual_state == "OPCIONES":
        #dibujo los botones
        menu_opciones.draw()
        #para el efecto hower
        menu_opciones.update_color(mouse_position)


    #actualizar la pantalla
    pg.display.update()

    #fps
    time.tick(30)

#cierro por completo el funcionamiento e pygame
pg.quit()
