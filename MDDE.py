#importaciones
import pygame as pg
import os
from archivos_necesarios import main_menu, botones, constantes, functions, caja_de_texto, game

#pestaña principal
pg.init()
screen = pg.display.set_mode((1280,720))
titulo = pg.display.set_caption("MDDE")
time = pg.time.Clock()
run = True

#estados del juego
actual_state = "PRINCIPAL_MENU"
sub_state = ""

#cargamos los menus
menu_principal = main_menu.mainmenu(screen)
menu_opciones = main_menu.opciones(screen)
en_juego = game.play(screen)
menu_pausa = game.pausa(screen)
text_box = caja_de_texto.text_box(screen)

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

                    if opcion_seleccionada == "New Game":
                        actual_state = "JUEGO"

                        #si se llega a darle al boton pause cuando se esta en el juego

                    if opcion_seleccionada == "Exit":
                        run = False

                #para cuando estamos en el menu de opciones
                elif actual_state == "OPCIONES":
                    opcion_seleccionada = menu_opciones.manage_click(pos_click)

                    if opcion_seleccionada == "Exit":
                        actual_state = "PRINCIPAL_MENU"

                elif sub_state == "PAUSA" and actual_state == "JUEGO":
                    #si se llega a darle a alguno de los botones del menu pausa
                    opcion_seleccionada = menu_pausa.manage_click(pos_click)

                    if opcion_seleccionada == "Return to game":
                        sub_state = "JUGAR"

                    elif opcion_seleccionada == "Return main menu":
                        sub_state = "PRINCIPAL_MENU"
                        actual_state = "PRINCIPAL_MENU"

                elif actual_state == "JUEGO" and sub_state != "PAUSA":
                    #si se llega a darle al boton pause cuando se esta en el juego
                    opcion_seleccionada = en_juego.manage_click(pos_click)
                    if opcion_seleccionada == "Pause":

                        #Para poder abrir el boton de pausa del juego
                        sub_state = "PAUSA"

                

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

    elif actual_state == "JUEGO":
        #dibujo los botones
        en_juego.draw()
        #dibujo la caja dee texto
        text_box.draw()

        #para que no se reproduzca el efecto hower mientras el juego este pausado
        if sub_state != "PAUSA":
            #para el efecto hower
            en_juego.update_color(mouse_position)
            
        #para dibujar el menu de pausa
        if sub_state == "PAUSA":
            #dibujo los botones y el fondo del menu pausa
            menu_pausa.draw()
            #para el efecto hower
            menu_pausa.update_color(mouse_position)

    #actualizar la pantalla
    pg.display.update()

    #fps
    time.tick(30)

#cierro por completo el funcionamiento e pygame
pg.quit()
