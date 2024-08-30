# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:37:44 2024

@author: Eduardo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen con distorsión
image = cv2.imread('C:/Users/Eduardo/OneDrive - Grupo UniCCo/Clases UP (Licenciatura)/imagenes/fotografo.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Mostrar la imagen original con distorsión
plt.figure(figsize=(8, 6))
plt.title("Imagen con Distorsión")
plt.imshow(image)
plt.show()

# Definir la matriz de la cámara
h, w = image.shape[:2]
focal_length = w  # Supongamos que la longitud focal es igual al ancho de la imagen
center = (w / 2, h / 2)
camera_matrix = np.array([[focal_length, 0, center[0]],
                          [0, focal_length, center[1]],
                          [0, 0, 1]])

# Coeficientes de distorsión: [k1, k2, p1, p2, k3]
dist_coeffs = np.array([-0.3, 0.1, 0, 0, 0])

# Corregir la distorsión
undistorted_image = cv2.undistort(image, camera_matrix, dist_coeffs)

# Mostrar la imagen corregida
plt.figure(figsize=(8, 6))
plt.title("Imagen Corregida")
plt.imshow(undistorted_image)
plt.show()
