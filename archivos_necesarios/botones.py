import pygame as pg
from archivos_necesarios import constantes
import os
from archivos_necesarios import functions
from archivos_necesarios import game

class buttons:
    def __init__(self, screen, texto, x, y, posicion_ini="topleft", ancho=160,alto=40):
        #tomamos la pantalla del juego
        self.screen = screen

        #tomamos el nombre de la opcion
        self.name_id = texto

        #fuente inicial del texto
        self.text = pg.font.SysFont("Arial",20)
        #renderizamos el texto
        self.text_render = self.text.render(texto,True,constantes.NEGRO)
        
        #para hacer el efecto de cuando pasamos el cursor encima del boton (cambiar de color el boton)
        self.color_rect_nuevo = constantes.NEGRO
        
        #creamos el rectangulo en la posicion que se nos da
        self.hitbox = functions.position_rect(x,y, posicion_ini, ancho, alto)

        #centramos el texto en donded va a estar el rectangulo
        self.text_center = self.text_render.get_rect()
        self.text_center.center = self.hitbox.center

    def update_color(self, mouse_position):
        #tomamos la posicion del mouse actualizada
        #hago un if para que verifique si el raton esta puesto en el boton
        if self.hitbox.collidepoint(mouse_position):
            #este nuevo color será el que reemplaze el negro si es que el mouse esta por encima del cuadro
            self.color_rect_nuevo = constantes.ROJO
        else:
            self.color_rect_nuevo = constantes.NEGRO

    #creamos la funcion dibujar para poder mostrar en pantalla los botones
    def draw(self):
         #dibujamos el rectangulo
        pg.draw.rect(self.screen, self.color_rect_nuevo ,self.hitbox,2)

        #dibujamos el texto
        self.screen.blit(self.text_render, self.text_center)

    #hago una funcion que tome cuando se le da click a una opcion
    def click_buttom(self, mouse_position):
        #tomo la poisicion del mouse
        if self.hitbox.collidepoint(mouse_position):
            return True