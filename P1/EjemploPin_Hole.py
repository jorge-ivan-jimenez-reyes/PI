# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:51:34 2024

@author: Eduardo
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def simular_pin_hole(imagen, tamano_pin_hole):
    kernel = np.ones((tamano_pin_hole, tamano_pin_hole), np.float32) / (tamano_pin_hole ** 2)
    return cv2.filter2D(imagen, -1, kernel)

# Cargar la imagen
imagen = cv2.imread('C:/Users/Eduardo/OneDrive - Grupo UniCCo/Clases UP (Licenciatura)/imagenes/fotografo.png', cv2.IMREAD_GRAYSCALE)

# Simular pin-hole con diferentes tamaños
imagen_pin_hole_1 = simular_pin_hole(imagen, 3)
imagen_pin_hole_2 = simular_pin_hole(imagen, 5)

# Mostrar las imágenes
plt.figure(figsize=(10,5))
plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(imagen, cmap='gray')

plt.subplot(1, 3, 2)
plt.title("Pin-hole 3x3")
plt.imshow(imagen_pin_hole_1, cmap='gray')

plt.subplot(1, 3, 3)
plt.title("Pin-hole 5x5")
plt.imshow(imagen_pin_hole_2, cmap='gray')

plt.show()
