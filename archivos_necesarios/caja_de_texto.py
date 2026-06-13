#importaciones
import pygame as pg
import os
from archivos_necesarios import main_menu, botones, constantes, functions, game

#clase de la caja de texto
class text_box:
    def __init__(self,screen):
        #tomamos la pantalla
        self.screen = screen
        #hago el tamaño que tendra la caja de texto y tambien su posicion
        self.size_text_box = functions.position_rect(1280/2,716,"midbottom",1080,216)
    
    def draw(self):
        #dibujo la caja de texto
        pg.draw.rect(self.screen, constantes.NEGRO, self.size_text_box,2)
