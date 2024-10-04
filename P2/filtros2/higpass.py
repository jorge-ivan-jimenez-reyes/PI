import cv2
import numpy as np


img = cv2.imread(r'C:\Users\jorge\Desktop\UP_Jorge\ProcesamientoImagenes\P2\filtros2\megaminion.png')


kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

# Aplicar el filtro
high_pass = cv2.filter2D(img, -1, kernel)

# Guardar la imagen filtrada
cv2.imwrite('megaminions.png', high_pass)
