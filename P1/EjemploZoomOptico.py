# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:21:41 2024

@author: Eduardo
"""

from PIL import Image

def aplicar_zoom_optico(imagen, nivel_zoom):
    ancho, alto = imagen.size
    nueva_ancho = int(ancho / nivel_zoom)
    nueva_alto = int(alto / nivel_zoom)
    
    izquierda = (ancho - nueva_ancho) // 2
    superior = (alto - nueva_alto) // 2
    derecha = (ancho + nueva_ancho) // 2
    inferior = (alto + nueva_alto) // 2
    
    imagen_zoom = imagen.crop((izquierda, superior, derecha, inferior))
    return imagen_zoom.resize(imagen.size, Image.LANCZOS)

# Cargar la imagen
imagen = Image.open('C:/Users/Eduardo/OneDrive - Grupo UniCCo/Clases UP (Licenciatura)/imagenes/fotografo.png')

# Aplicar zoom óptico simulado
nivel_zoom = 2  # Nivel de zoom (2x, 3x, etc.)
imagen_zoom = aplicar_zoom_optico(imagen, nivel_zoom)

# Mostrar la imagen con zoom
imagen_zoom.show()
