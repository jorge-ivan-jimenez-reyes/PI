import cv2
import numpy as np

img = cv2.imread(r'C:\Users\jorge\Desktop\UP_Jorge\ProcesamientoImagenes\P2\filtros2\megaminion.png')

low = cv2.GaussianBlur(img, (17, 17), 0)

high = cv2.subtract(img, low)

band_stop = cv2.add(img, high)

cv2.imwrite('imagen_rechaza_banda.jpg', band_stop)
