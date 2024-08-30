from PIL import Image
import numpy as np

img = Image.open('megaminions.png')
img_np = np.array(img)

if img_np.shape[-1] == 4:
    img_np = img_np[..., :3]
    