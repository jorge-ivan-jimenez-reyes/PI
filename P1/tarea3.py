

from PIL import Image, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt


def ajustar_brillo(img, factor):
    
    img_modificada = img.copy()
    
    ancho, alto = img.size
    
    
    for x in range(ancho):
        for y in range(alto):
            
            pixel = img.getpixel((x, y))
            
            
            if len(pixel) == 4:
                r, g, b, a = pixel  
            else:
                r, g, b = pixel  

            
            r = int(r * factor)
            g = int(g * factor)
            b = int(b * factor)
            
            
            r = min(255, max(0, r))
            g = min(255, max(0, g))
            b = min(255, max(0, b))
            
            
            if len(pixel) == 4:
                img_modificada.putpixel((x, y), (r, g, b, a))  # Mantener el canal alfa
            else:
                img_modificada.putpixel((x, y), (r, g, b))  # Sin canal alfa
    
    return img_modificada

# Función para ajustar el brillo usando ImageEnhance
def ajustar_brillo_enhance(img, factor):
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)

# Función para ajustar el brillo usando NumPy
def ajustar_brillo_numpy(img, factor):
    img_array = np.array(img)
    img_array = np.clip(img_array * factor, 0, 255).astype(np.uint8)
    return Image.fromarray(img_array)

# Cargar la imagen original
img = Image.open('megaminions.png')

# Mostrar la imagen original
plt.figure(figsize=(15, 5))

# Imagen original
plt.subplot(1, 4, 1)
plt.title("Imagen Original")
plt.imshow(img)

# Aumentar el brillo (enfoque manual)
img_brillete_aumentado_manual = ajustar_brillo(img, 1.5)
plt.subplot(1, 4, 2)
plt.title("Brillo Aumentado (Manual)")
plt.imshow(img_brillete_aumentado_manual)

# Disminuir el brillo (enfoque manual)
img_brillete_disminuido_manual = ajustar_brillo(img, 0.5)
plt.subplot(1, 4, 3)
plt.title("Brillo Disminuido (Manual)")
plt.imshow(img_brillete_disminuido_manual)

# Aumentar el brillo (usando ImageEnhance)
img_brillete_aumentado_enhance = ajustar_brillo_enhance(img, 1.5)
plt.subplot(1, 4, 4)
plt.title("Brillo Aumentado (Enhance)")
plt.imshow(img_brillete_aumentado_enhance)

plt.show()
