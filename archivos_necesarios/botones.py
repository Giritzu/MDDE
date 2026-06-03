import pygame as pg
from archivos_necesarios import constantes
import os

class buttons:
    def __init__(self, screen):
        #tomamos la pantalla del juego
        self.screen = screen

        #el texto
        self.text = pg.font.SysFont("Arial",20)
        self.text_render = self.text.render(None,True,constantes.NEGRO)
        self.text_coords = screen.blit(self.text_render,(0,0))

class boton_play(buttons):
    def __init__(self, screen):
        super().__init__(screen)
        self.text_render = self.text.render("Nuevo juego",True, constantes.NEGRO)
        self.text_coords = screen.blit(self.text_render,(100,340))

class boton_load(buttons):
    def __init__(self, screen):
        super().__init__(screen)
        self.text_render = self.text.render("Cargar datos",True, constantes.NEGRO)
        self.text_coords = screen.blit(self.text_render,(150,340+70))

class boton_extras(buttons):
    def __init__(self, screen):
        super().__init__(screen)
        self.text_render = self.text.render("Extras",True, constantes.NEGRO)
        self.text_coords = screen.blit(self.text_render,(150+50,340+70+70))

class boton_opciones(buttons):
    def __init__(self, screen):
        super().__init__(screen)
        self.text_render = self.text.render("Opciones",True, constantes.NEGRO)
        self.text_coords = screen.blit(self.text_render,(150+50+50,340+70+70+70))

class boton_exit(buttons):
    def __init__(self, screen):
        super().__init__(screen)
        self.text_render = self.text.render("Salir",True, constantes.NEGRO)
        self.text_coords = screen.blit(self.text_render,(150+50+50+50,340+70+70+70+70))