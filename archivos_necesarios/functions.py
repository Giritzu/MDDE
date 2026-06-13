import pygame as pg
import os
from archivos_necesarios import main_menu, botones, constantes, caja_de_texto, game

##carpeta meramente hecha para tener todas las funciones necesarias para reciclar codigo

##funcion para los rectangulos (hitboxes) de los botones y todo lo que se vaya a usar relacionados con estos (solo los va a crear mas no dibujar)
def position_rect(x,y, posicion_predefinida="center",ancho=160,alto=40):
    #crearemos primero el rectangulo en el punto 0.0 para que solo simplemente tengamos que moverlo a la posicion que deseo.
    rectangle = pg.Rect(0,0,ancho,alto)
    #posicionaremos el rectangulo
    setattr(rectangle, posicion_predefinida,(x,y))
    
    return rectangle
##pa probar rapidamente los rectangulos
def position_rect_y_dibujo(screen,color,ancho,alto,x,y, posicion_predefinida="center"):
    #crearemos primero el rectangulo en el punto 0.0 para que solo simplemente tengamos que moverlo a la posicion que deseo.
    rectangle = pg.Rect(0,0,ancho,alto)
    #posicionaremos el rectangulo
    setattr(rectangle, posicion_predefinida,(x,y))
    #dibujamos el rectangulo
    pg.draw.rect(screen, color, rectangle, 2)
    return rectangle


##funcion para los textos (por ahora la dejare existiendo)
def text_renders(text,pantalla, text_color,text_option,x,y):
    
    pass