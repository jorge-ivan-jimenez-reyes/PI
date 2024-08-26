from PIL import Image
import numpy as np

# Cargar la imagen
img = Image.open('megaminions.png')
img_np = np.array(img)

# Verificar si la imagen tiene un canal alfa y eliminarlo si es necesario
if img_np.shape[-1] == 4:
    img_np = img_np[..., :3]  # Elimina el canal alfa

# Definir el rango de colores para segmentar el color amarillo
lower_yellow = np.array([200, 180, 0])
upper_yellow = np.array([255, 255, 150])

# Crear una imagen en blanco con las mismas dimensiones
mask = np.zeros_like(img_np)

# Recorrer pixel por pixel
for i in range(img_np.shape[0]):
    for j in range(img_np.shape[1]):
        pixel = img_np[i, j]
        if np.all(pixel >= lower_yellow) and np.all(pixel <= upper_yellow):
            mask[i, j] = pixel

# Convertir el resultado en una imagen
result_img = Image.fromarray(mask)
   
# Guardar la imagen segmentada
result_img.save('imagen_segmentada_yellow.png')

# Mostrar la imagen original y la imagen segmentada
img.show()
result_img.show()
