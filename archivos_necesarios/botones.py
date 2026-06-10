import pygame as pg
from archivos_necesarios import constantes
import os
from archivos_necesarios import functions

class buttons:
    def __init__(self, screen, texto, x, y, posicion_ini="topleft"):
        #tomamos la pantalla del juego
        self.screen = screen
        #fuente inicial del texto
        self.text = pg.font.SysFont("Arial",20)
        #renderizamos el texto
        self.text_render = self.text.render(texto,True,constantes.NEGRO)
        
        #creamos el rectangulo en la posicion que se nos da
        self.hitbox = functions.position_rect(160,40,x,y, posicion_ini)

        #centramos el texto en donded va a estar el rectangulo
        self.text_center = self.text_render.get_rect()
        self.text_center.center = self.hitbox.center

    #creamos la funcion dibujar para poder mostrar en pantalla los botones
    def draw(self):
        #dibujamos el rectangulo
        pg.draw.rect(self.screen, constantes.NEGRO,self.hitbox,2)

        #dibujamos el texto
        self.screen.blit(self.text_render, self.text_center)
