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
    plt.savefig('Imadjust.png',dpi=1200)
    plt.show()
   # plt.savefig(nombre_del_archivo, bbox_inches='tight')

    return None
def imadjust(x,a,b,c,d,gamma=1):
    y = (((x - a) / (b - a)) ** gamma) * (d - c) + c
    return y
image = Image.open('38.1.jpg')
if image.mode != 'L':
    image=image.convert('L')
histograma=image.histogram()
plt.imshow(image,cmap='gray')
plt.show()
graficar(histograma)
arr = np.asarray(image)
arr2=imadjust(arr,arr.min(),arr.max(),0,1)

fig = plt.figure()
plt.imshow(arr2,cmap='gray')
plt.axis('off')
plt.savefig('temp.jpg',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.show()
image = Image.open('temp.jpg')
if image.mode != 'L':
    image=image.convert('L')
histograma=image.histogram()
graficar(histograma)