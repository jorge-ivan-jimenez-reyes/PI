# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:05:54 2024

@author: Eduardo
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def aplicar_filtro_sepia(imagen):
    # Crear un kernel para el filtro sepia
    filtro_sepia = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    
    
   # filtro_sepia = np.array([[0.1, 0.1, 0.1],
    #                         [0.1, 0.1, 0.1],
     #                        [0.1, 0.1, 0.1]])
    
    
    
    # Aplicar el filtro sepia a la imagen
    imagen_sepia = cv2.transform(imagen, filtro_sepia)
    return np.clip(imagen_sepia, 0, 255).astype(np.uint8)

# Cargar la imagen
imagen = cv2.imread('C:/Users/Eduardo/OneDrive - Grupo UniCCo/Clases UP (Licenciatura)/imagenes/flowers.jpg')

# Aplicar filtro sepia
imagen_sepia = aplicar_filtro_sepia(imagen)

# Mostrar la imagen original y con el filtro sepia
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title("Filtro Sepia")
plt.imshow(cv2.cvtColor(imagen_sepia, cv2.COLOR_BGR2RGB))

plt.show()
