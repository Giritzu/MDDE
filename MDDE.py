#importaciones
import pygame as pg
import os

#pestaña principal
pg.init()
screen = pg.display.set_mode((1280,720))
titulo = pg.display.set_caption("MDDE")
time = pg.time.Clock()
run = True

#codigo principal
while run == True:
    #si le dan a quit para poder salir del juego
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            run = False
pg.quit()
