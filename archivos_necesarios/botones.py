import pygame as pg
from archivos_necesarios import constantes
import os
from archivos_necesarios import functions

class buttons:
    def __init__(self, screen, texto, x, y, posicion_ini="topleft"):
        #tomamos la pantalla del juego
        self.screen = screen

        #tomamos la posicion del mouse
        self.mouse_position = pg.mouse.get_pos()

        #fuente inicial del texto
        self.text = pg.font.SysFont("Arial",20)
        #renderizamos el texto
        self.text_render = self.text.render(texto,True,constantes.NEGRO)
        
        #para hacer el efecto de cuando pasamos el cursor encima del boton (cambiar de color el boton)
        self.color_rect_nuevo = constantes.NEGRO
        
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

    def update_color(self):
        #tomamos la posicion del mouse actualizada
        self.mouse_position = pg.mouse.get_pos()
        #hago un if para que verifique si el raton esta puesto en el boton
        if self.hitbox.collidepoint(self.mouse_position):
            #este nuevo color será el que reemplaze el negro si es que el mouse esta por encima del cuadro
            self.color_rect_nuevo = constantes.ROJO
        else:
            self.color_rect_nuevo = constantes.NEGRO
        
        #dibujamos el cuadro
        pg.draw.rect(self.screen, self.color_rect_nuevo, self.hitbox,2)