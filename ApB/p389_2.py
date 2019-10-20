# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
import ctypes
import win32con
 
def setWallpaperWithCtypes(path):
    cs = ctypes.c_buffer(path)
    ok = ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER, 0, cs, 0)
 
if __name__ == "__main__":
    path = b'C:\Users\Arturo\Pictures\WallPapers\paisaje.jpg'
    setWallpaperWithCtypes(path)
    