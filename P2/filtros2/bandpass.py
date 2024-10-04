import cv2
import numpy as np

img = cv2.imread(r'C:\Users\jorge\Desktop\UP_Jorge\ProcesamientoImagenes\P2\filtros2\megaminion.png')


low = cv2.GaussianBlur(img, (17, 17), 0)


band_pass = cv2.subtract(img, low)

# Guardar la imagen filtrada
cv2.imwrite('imagen_pasa_banda.jpg', band_pass)
