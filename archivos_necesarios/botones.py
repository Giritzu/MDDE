import pygame as pg
from archivos_necesarios import constantes
import os

class buttons:
    def __init__(self, screen):
        #tomamos la pantalla del juego
        self.screen = screen

        #el texto
        self.text = pg.font.SysFont("Arial",20)
        self.text_render = self.text.render("Play",True,constantes.NEGRO)
        self.text_coords = screen.blit(self.text_render,(0,0))

class boton_play(buttons):
    def __init__(self, screen):
        super().__init__(screen)
        self.text_coords = screen.blit(self.text_render,(50,340))