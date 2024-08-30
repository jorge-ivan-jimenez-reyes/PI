# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:56:08 2024

@author: Eduardo
"""

def calcular_distancia_hiperfocal(f, N, c):
    return (f ** 2) / (N * c) + f

# Parámetros de la cámara
f = 50  # Longitud focal en mm
N = 8  # Número f (apertura)
c = 0.03  # Círculo de confusión en mm

# Calcular la distancia hiperfocal
distancia_hiperfocal = calcular_distancia_hiperfocal(f, N, c)

print(f"Distancia Hiperfocal: {distancia_hiperfocal:.2f} mm")
