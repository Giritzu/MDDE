import pygame as pg
import os
from archivos_necesarios import constantes
#hago la clase main menu la cual tendra las opciones iniciales deljuego, play, options, extras, exit.
class mainmenu:
    def __init__(self, screen):
        #para tomar la pantalla del juego
        self.screen = screen
        #el texto de los botones
        self.bg_color = (100,100,200)
        #color base de pruebas
        self.screen.fill(self.bg_color)
        #
    #para dibujar un fondo sencillo por los momentos
    def draw(self):
        pass

class opciones(mainmenu):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.bg_font = (255,200,255)
