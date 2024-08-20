import time
from PIL import Image

def negativo_grises2(im):
    tiempoIn=time.time()
    ruta = ("./imagenes/"+im)
    imagen = Image.open(ruta)
    im.show()
    im15 = im.copy()
    im15 = im15.convert('L')
    width, height = im15.size
    im15.show()

    