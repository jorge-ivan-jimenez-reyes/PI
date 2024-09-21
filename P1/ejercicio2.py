import cv2
import numpy as np
import matplotlib.pyplot as plt

def mostrar_imagen(titulo, imagen):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.title(titulo)
    plt.axis('off')
    plt.show()

def transformacion_logaritmica(imagen):

    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    c = 255 / np.log(1 + np.max(imagen_gris))
    imagen_logaritmica = c * (np.log(imagen_gris + 1))
    
    imagen_logaritmica = np.array(imagen_logaritmica, dtype=np.uint8)
    
    mostrar_imagen("Imagen Original", imagen)
    mostrar_imagen("Transformación Logarítmica", imagen_logaritmica)
    
    return imagen_logaritmica

# Cargamos una imagen genérica
imagen = cv2.imread('megaminion.png')

# Aplicamos la transformación logarítmica
imagen_log = transformacion_logaritmica(imagen)
