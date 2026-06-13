#importaciones
import pygame as pg
import os
from archivos_necesarios import main_menu
from archivos_necesarios import botones
from archivos_necesarios import constantes
from archivos_necesarios import functions


#en este archivo estara la clase new game y load game.

#clase cuando se este jugando el juego
class play:
    def __init__(self, screen):
        #tomo la pantalla
        self.screen = screen
        #el taamaño del menu
        self.screen_resolution = (0,0,1280,720)

        #el color del fondo
        self.bg_color = constantes.AMARILLO_CLARO

        #estaran los botones que tendra el juego ya empezado
        self.option_ingametext = ["Pause", "Esconder opciones y menus"]
        
        #la creacion de los menus (la lista)
        self.options_ingame = []

        #un for in para crearlas todas y posicionarlas
        for i, texto in enumerate(self.option_ingametext):
            #tamaño del rectangulo (lo hare un cuadrado, ya que son botones chicos)
            lado_uno = 40
            lado_dos = 40
            #la diferencia de las posiciones de los botones
            position_x = 1270 - (i*(1260-lado_uno))

            #creamos los cuadrados
            self.options = botones.buttons(screen, texto, position_x, 10,"topright", lado_uno, lado_dos)
            #los guardamos en la lista
            self.options_ingame.append(self.options)

    #para dibujar tanto el menu como los botones
    def draw (self):
        #dibujamos el color del fondo
        pg.draw.rect(self.screen,self.bg_color, self.screen_resolution)

        #dibujamos los botones
        for boton in self.options_ingame:
            boton.draw()

    #funcion para el cambio de color al pasar el mouse sobre el boton
    def update_color(self,mouse_position):
        #para dibujar todos los botonescon los nuevos colores
        for boton in self.options_ingame:
            boton.update_color(mouse_position)
    
    #funcion para manejar los clicks sobre los botones
    def manage_click(self, mouse_position):
        #obtengo las opciones de la lista self.options
        for opcion in self.options_ingame:
            if opcion.click_buttom(mouse_position):
                return opcion.name_id
            
#hare la case en donde se inicia el juego, esta clase lo que va a hacer es controlar el fondo, y tener el boton pausa
#el trabajo del boton pausa va a ser un submenu el cual van a estar opciones similares a las dele main_menu

class pausa:
    def __init__(self):
        pass