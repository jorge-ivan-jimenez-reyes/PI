# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:57:26 2024

@author: Eduardo
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

def simular_aberracion_esferica(imagen):
    h, w = imagen.shape[:2]
    x = np.linspace(-1, 1, w)
    y = np.linspace(-1, 1, h)
    X, Y = np.meshgrid(x, y)
    dist = np.sqrt(X**2 + Y**2)
    aberracion = 1 + 0.3 * dist**2
    
    # Expandir aberracion para que coincida con los canales de la imagen
    aberracion = np.repeat(aberracion[:, :, np.newaxis], 3, axis=2)
    
    return cv2.warpPolar(imagen, (w, h), (w//2, h//2), w//2, cv2.WARP_FILL_OUTLIERS) * aberracion

def simular_aberracion_cromatica(imagen):
    b, g, r = cv2.split(imagen)
    g = cv2.warpAffine(g, np.float32([[1, 0, 2], [0, 1, 2]]), (g.shape[1], g.shape[0]))
    r = cv2.warpAffine(r, np.float32([[1, 0, 4], [0, 1, 4]]), (r.shape[1], r.shape[0]))
    return cv2.merge([b, g, r])

# Cargar la imagen
imagen = cv2.imread('C:/Users/Eduardo/OneDrive - Grupo UniCCo/Clases UP (Licenciatura)/imagenes/flowers.jpg')

# Simular aberraciones
imagen_esferica = simular_aberracion_esferica(imagen)
imagen_cromatica = simular_aberracion_cromatica(imagen)

# Mostrar las imágenes
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Imagen Original")
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 2)
plt.title("Aberración Esférica")
plt.imshow(cv2.cvtColor(imagen_esferica.astype(np.uint8), cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 3)
plt.title("Aberración Cromática")
plt.imshow(cv2.cvtColor(imagen_cromatica, cv2.COLOR_BGR2RGB))

plt.show()




