# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:54:10 2024

@author: Eduardo
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def simular_profundidad_campo(imagen, plano_enfoque, desenfoque):
    mask = np.zeros_like(imagen)
    cv2.rectangle(mask, (0, plano_enfoque), (imagen.shape[1], imagen.shape[0]), (255, 255, 255), -1)
    
    imagen_blur = cv2.GaussianBlur(imagen, (desenfoque, desenfoque), 0)
    return np.where(mask==255, imagen, imagen_blur)

# Cargar la imagen
imagen = cv2.imread('C:/Users/Eduardo/OneDrive - Grupo UniCCo/Clases UP (Licenciatura)/imagenes/fotografo.png')

# Simular profundidad de campo
plano_enfoque = 200  # Línea en la que todo estará enfocado
desenfoque = 21  # Cantidad de desenfoque para simular DOF

imagen_dof = simular_profundidad_campo(imagen, plano_enfoque, desenfoque)

# Mostrar la imagen con profundidad de campo simulada
plt.figure(figsize=(10,5))
plt.title("Profundidad de Campo Simulada")
plt.imshow(cv2.cvtColor(imagen_dof, cv2.COLOR_BGR2RGB))
plt.show()
