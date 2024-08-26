from PIL import Image
import numpy as np

# Cargar la imagen
img = Image.open('megaminions.png')
img_np = np.array(img)

# Verificar si la imagen tiene un canal alfa y eliminarlo si es necesario
if img_np.shape[-1] == 4:
    img_np = img_np[..., :3]  # Elimina el canal alfa

# Definir el rango de colores a segmentar (por ejemplo, para un objeto rojo)
lower_color = np.array([0, 0, 100])
upper_color = np.array([50, 50, 255])

# Crear una imagen en blanco con las mismas dimensiones
mask = np.zeros_like(img_np)

# Recorrer pixel por pixel
for i in range(img_np.shape[0]):
    for j in range(img_np.shape[1]):
        pixel = img_np[i, j]
        if np.all(pixel >= lower_color) and np.all(pixel <= upper_color):
            mask[i, j] = pixel

# Convertir el resultado en una imagen
result_img = Image.fromarray(mask)
   
# Guardar la imagen segmentada
result_img.save('imagen_segmentada.png')

# Mostrar la imagen original y la imagen segmentada
img.show()
result_img.show()
