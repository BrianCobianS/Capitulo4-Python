#4 procesamiento   "Contraste automatico"
import matplotlib.pyplot as plt
import numpy as np
#IMAGEN 1
Imagen='1.jpg'
I=plt.imread(Imagen)
plt.title('Imagen original')
plt.imshow(I)
plt.show()
rgb = [0.2989, 0.5870, 0.1140]
ig = np.dot(I[...,:3], rgb)
minimos=[]
maximos=[]
for x in range(len(ig)):
    minimos.append(min(ig[x]))
    maximos.append(max(ig[x]))
minimo=min(minimos)
maximo=max(maximos)
AC=[]
for x in range(len(ig)):
    for h in range(len(ig[x])):
            ig[x][h]=((ig[x][h]-minimo)*(255/maximo-minimo))
            if ig[x][h]>=256: 
                ig[x][h]=255
            ig[x][h]=ig[x][h]*-1
            AC.append(ig[x][h])
plt.imshow(ig,cmap='gray')
plt.title("Contraste automatico")
plt.show()
intervalos = range(round(min(AC)), round(max(AC)) + 2) #calculamos los extremos de los intervalos
plt.hist(x=AC, bins=intervalos, color='b', rwidth=0.85)
plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
plt.title('Histogram AC')
plt.xlabel('Intensity values')
plt.ylabel('Number of pixels')
plt.savefig('HistAC.png',dpi=1200)
plt.show()
