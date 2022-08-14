
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def graficar(datos):
    plt.figure(1)
    x=range(len(datos))
    plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
    plt.bar(x, datos, align='center')
    plt.title('Histogram')
    plt.xlabel('Intensity values')
    plt.ylabel('Number of pixels')
    plt.savefig('Histograma.png',dpi=1200)
    plt.show()
  

    return None

#IMAGEN 1
Imagen='25.jpg'
I=plt.imread(Imagen)
plt.title('Imagen original')
plt.imshow(I)
plt.show()

#3 procesamiento segmentacion  
rgb = [0.2989, 0.5870, 0.1140]
ig = np.dot(I[...,:3], rgb)
h2=[] 
h1=[]
for x in range(len(ig)):
    for h in range(len(ig[x])):
            h2.append(int(ig[x][h]))
            if ig[x][h] <=60:
                ig[x][h]=0
for x in range(len(h2)):
    if h2[x-1]<60:
        h2[x-1]=0
for x in h2:
    if x != 0:
        h1.append(x)
plt.imshow(ig,cmap='gray')
plt.axis('off')
plt.savefig('segmentacion.png',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.title("Segmentacion por umbral")
plt.savefig('temp', bbox_inches='tight')
plt.show()
intervalos = range(round(min(h1)), round(max(h1)) + 2) #calculamos los extremos de los intervalos
plt.hist(x=h1, bins=intervalos, color='b', rwidth=0.85)
plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
plt.title('Histogram')
plt.xlabel('Intensity values')
plt.ylabel('Number of pixels')
plt.savefig('Histograma.png',dpi=1200)
plt.show()