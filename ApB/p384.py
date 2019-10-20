# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
import pygame
import pygame.sprite.Sprite as Sprite

class SimpleAnimation(Sprite):
    """ Clase para animar mediante la composición de varias imágenes """
 
    def __init__(self, frames):
        Sprite.__init__(self)
        self.frames = frames    # los "frames" de la animación
        self.current = 0        # índice del frame actual
        self.image = frames[0]  # imagen (frame) por defecto
        self.rect = self.image.get_rect()    # límites del sprite
        self.playing = 0
         
    def update(self, *args):
        if self.playing:    # animar si el juego está en marcha
            self.current += 1
            if self.current == len(self.frames):
                self.current = 0
            self.image = self.frames[self.current]
            # solo es necesario si el tamaño del frame cambia
            self.rect = self.image.get_rect(center=self.rect.center)

