import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#IMAGEN 1
Imagen='47.jpg'
Imagen2='53.jpg'
I=plt.imread(Imagen)
rgb = [0.2989, 0.5870, 0.1140]
ig = np.dot(I[...,:3], rgb)
plt.imshow(ig,cmap='gray')
plt.axis('off')
plt.savefig('b&w1.png',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.title('Imagen 1 a escala de grises')
plt.show()

I2=plt.imread(Imagen2)
rgb = [0.2989, 0.5870, 0.1140]
ig2 = np.dot(I2[...,:3], rgb)
plt.imshow(ig2,cmap='gray')
plt.axis('off')
plt.savefig('b&w2.png',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.title('Imagen 2 a escala de grises')
plt.show()

#1 procesamiento
#Este for sirve para aumentar o disminuir el brillo mediante la multipliacaion de la informaicon de los pixels
# for x in range(len(IC)):
for x in range(len(ig)):
    for h in range(len(ig[x])):
            ig[x][h]=ig[x][h]-ig2[x][h]
            if ig[x][h]>=256: 
                ig[x][h]=255
plt.imshow(ig,cmap='gray')
plt.axis('off')
plt.savefig('Resta.png',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.title('Imagenes sumadas')
plt.show()