
import matplotlib.pyplot as plt
import numpy as np

#IMAGEN 1
Imagen='33.jpg'
I=plt.imread(Imagen)
plt.title('Imagen original')
plt.imshow(I)
plt.show()

rgb = [0.2989, 0.5870, 0.1140]
ig = np.dot(I[...,:3], rgb)
plt.imshow(ig,cmap='gray')
plt.axis('off')
plt.savefig('b&w.png',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.title('Imagen a escala de grises')
plt.show()

#ACCEDER AL RGB
rojo=[]
azul=[]
verde=[]
for x in range(round(len(I)/3)):
    for h in range(len(I[x])):
        for f in range(len(I[x][h])):
            rojo.append(I[x][h][0])
            azul.append(I[x][h][1])
            verde.append(I[x][h][2])
print(len(verde))
print(len(rojo))
print(len(azul))
intervalos = range(round(min(rojo)), round(max(rojo)) + 2) #calculamos los extremos de los intervalos
plt.hist(x=rojo, bins=intervalos, color='r', rwidth=0.85)
plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
plt.title('Histogram of Red')
plt.xlabel('Intensity values')
plt.ylabel('Number of pixels')
plt.savefig('Histogramarojo.png',dpi=1200)
plt.show()

intervalos = range(round(min(verde)), round(max(verde)) + 2) #calculamos los extremos de los intervalos
plt.hist(x=verde, bins=intervalos, color='y', rwidth=0.85)
plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
plt.title('Histogram of Green')
plt.xlabel('Intensity values')
plt.ylabel('Number of pixels')
plt.savefig('Histogra_verde.png',dpi=1200)
plt.show()
intervalos = range(round(min(azul)), round(max(azul)) + 2) #calculamos los extremos de los intervalos
plt.hist(x=azul, bins=intervalos, color='b', rwidth=0.85)
plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
plt.title('Histogram of Blue')
plt.xlabel('Intensity values')
plt.ylabel('Number of pixels')
plt.savefig('Histogra_azul.png',dpi=1200)
plt.show()

