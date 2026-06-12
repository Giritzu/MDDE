import pygame as pg
import os
from archivos_necesarios import constantes
from archivos_necesarios import botones
from archivos_necesarios import functions
#hago la clase main menu la cual tendra las opciones iniciales deljuego, play, options, extras, exit.
class mainmenu:
    def __init__(self, screen):
        #para tomar la pantalla del juego
        self.screen = screen
        #resolucion de la pantalla
        self.resolution = (0,0,1280,720)
        #el texto de los botones
        self.bg_color = (100,100,200)
        #color base de pruebas
       
        #opciones
        self.option_text = ["New Game", "Load Game", "Options", "Galery", "Creedits","Exit"]
        #guardaremos las opciones para despues dibujarlas en otra lista
        self.text_options = []

        for i, texto in enumerate(self.option_text):
            #posicion en y donde quiero cada boton para que esten separados simetricamentee
            position_y = 340 + (i*70)
            position_x = 90 + (i*80)
            #creo los rectangulos
            option = botones.buttons(screen, texto, position_x, position_y, "midbottom")
            #agrego los botones dibujados a la lista
            self.text_options.append(option)
        
     #creamos la funcion dibujar para poder mostrar en pantalla los botones
    def draw(self):
        #pintamos el fondo
        pg.draw.rect(self.screen, self.bg_color, self.resolution)

        #dibujamos los botones
        for boton in self.text_options:
            boton.draw()
    
    def update_color(self,mouse_position):
        #para dibujar todos los botonescon los nuevos colores
        for boton in self.text_options:
            boton.update_color(mouse_position)

    def manage_click(self, mouse_position):
        #obtengo las opciones de la lista self.options
        for opcion in self.text_options:
            if opcion.click_buttom(mouse_position):
                return opcion.name_id
"""
este sera la clase donde estaran la configuracion de volumen, textos, etc, este menu va a tener submenus con su configuracion
correspondiente
"""
class opciones:
    def __init__(self,screen):
        #colocamos la pantalla a la cual se está trabajando
        self.screen = screen
        
        #haremos el tamaño de la ventana, en este caso 1280*720
        self.screen_resolution = (0,0,1280,720)
        #color del fondo
        self.bg_color = constantes.GRIS

        #los submenus y botones que va a tener la lista
        self.options_text = ["Exit"]

        #los submenus pero en su version clase en una lista
        self.options_boton = []

        #este for es clave para que se creen los botones de manera automatica y eficiente
        for i, text in enumerate(self.options_text):
            
            #los posicionamos en el menu
            pos_y = 720 - (i*100)

            #creamos los rectangulos
            self.suboptions = botones.buttons(screen,text, 0, pos_y, "bottomleft")

            #lo metemos a nuestra lista de clase
            self.options_boton.append(self.suboptions)

    def draw (self):
        #dibujamos el color del fondo
        pg.draw.rect(self.screen,self.bg_color, self.screen_resolution)

        #dibujamos los botones
        for boton in self.options_boton:
            boton.draw()

    #para actualizar los colores de los botones
    def update_color(self):
        pass

    #para los clicks a los botones
    def manage_click(self, mouse_position):
        #obtengo las opciones de la lista self.options
        for opcion in self.options_boton:
            if opcion.click_buttom(mouse_position):
                return opcion.name_id