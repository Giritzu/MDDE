import pygame as pg
import os

#hago la clase main menu la cual tendra las opciones iniciales deljuego, play, options, extras, exit.
class mainmenu:
    def __init__(self, screen):
        #para tomar la pantalla del juego
        self.screen = screen
        #el texto de los botones
        self.wallpaper = screen.fill((0,0,0))
    
class opciones(mainmenu):
    def __init__(self, screen):
        super().__init__(screen)
