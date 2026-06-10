import pygame as pg
import os
from archivos_necesarios import constantes
from archivos_necesarios import botones

#hago la clase main menu la cual tendra las opciones iniciales deljuego, play, options, extras, exit.
class mainmenu:
    def __init__(self, screen):
        #para tomar la pantalla del juego
        self.screen = screen
        #resolucion de la pantalla
        self.resolution = (0,0,1280,720)
        #el texto de los botones
        self.bg_color = (100,100,200)
        #color base de pruebas
       
        #opciones
        option_text = ["New Game", "Load Game", "Options", "Galery", "Creedits","Exit"]
        #guardaremos las opciones para despues dibujarlas en otra lista
        self.text_options = []

        for i, texto in enumerate(option_text):
            #posicion en y donde quiero cada boton para que esten separados simetricamentee
            position_y = 340 + (i*70)
            position_x = 90 + (i*80)
            #creo los rectangulos
            option = botones.buttons(screen, texto, position_x, position_y, "midbottom")
            #agrego los botones dibujados a la lista
            self.text_options.append(option)
        
     #creamos la funcion dibujar para poder mostrar en pantalla los botones
    def draw(self):
        #pintamos el fondo
        pg.draw.rect(self.screen, self.bg_color, self.resolution)

        #dibujamos los botones
        for boton in self.text_options:
            boton.draw()

class opciones(mainmenu):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.bg_font = (255,200,255)
