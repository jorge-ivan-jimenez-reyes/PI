from PIL import Image
import matplotlib.pyplot as plt

# Función para ajustar el brillo pixel por pixel
def ajustar_brillo(img, factor):
    # Crear una copia de la imagen para modificar
    img_modificada = img.copy()
    # Obtener el tamaño de la imagen
    ancho, alto = img.size
    
    # Recorrer cada píxel de la imagen
    for x in range(ancho):
        for y in range(alto):
            # Obtener el valor del píxel
            pixel = img.getpixel((x, y))
            
            # Verificar si la imagen tiene un canal alfa (RGBA)
            if len(pixel) == 4:
                r, g, b, a = pixel  # Desempaquetar RGBA
            else:
                r, g, b = pixel  # Desempaquetar RGB

            # Ajustar cada canal de color según el factor
            r = int(r * factor)
            g = int(g * factor)
            b = int(b * factor)
            
            # Asegurarse de que los valores se mantengan en el rango [0, 255]
            r = min(255, max(0, r))
            g = min(255, max(0, g))
            b = min(255, max(0, b))
            
            # Asignar el nuevo valor al píxel
            if len(pixel) == 4:
                img_modificada.putpixel((x, y), (r, g, b, a))  # Mantener el canal alfa
            else:
                img_modificada.putpixel((x, y), (r, g, b))  # Sin canal alfa
    
    return img_modificada

# Cargar la imagen original
img = Image.open('megaminions.png')

# Mostrar la imagen original
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title("Imagen Original")
plt.imshow(img)

# Aumentar el brillo (por ejemplo, un factor de 1.5)
img_brillete_aumentado = ajustar_brillo(img, 1.5)
plt.subplot(1, 3, 2)
plt.title("Brillo Aumentado")
plt.imshow(img_brillete_aumentado)

# Disminuir el brillo (por ejemplo, un factor de 0.5)
img_brillete_disminuido = ajustar_brillo(img, 0.5)
plt.subplot(1, 3, 3)
plt.title("Brillo Disminuido")
plt.imshow(img_brillete_disminuido)

plt.show()
