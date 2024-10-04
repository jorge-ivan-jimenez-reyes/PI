import cv2
import numpy as np


img = cv2.imread(r'C:\Users\jorge\Desktop\UP_Jorge\ProcesamientoImagenes\P2\filtros2\megaminions.png')

kernel = np.ones((5, 5), np.float32) / 25

low_pass = cv2.filter2D(img, -1, kernel)

cv2.imwrite('imagen_pasa_bajas.jpg', low_pass)
