import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


#IMAGEN 1
Imagen='11.jpg'
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
            h1.append(ig[x][h])
h=0
while h < 15:
    x=0
    h2=[]
    while x< len(h1):
        if x%2==0:
           h2.append(h1[x]) 
        x+=1
    print("la longitud de la lista es h2 " + str(len(h2)))
    h1=h2
    h += 1
plt.imshow(ig,cmap='gray')
plt.axis('off')
plt.savefig('segmentacion.png',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.title("Segmentacion por umbral")
plt.savefig('temp', bbox_inches='tight')
plt.show()
intervalos = range(round(min(h2)), round(max(h2)) + 2) #calculamos los extremos de los intervalos
plt.hist(x=h2, bins=intervalos, color='b', rwidth=0.85)
plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
plt.title('Histogram')
plt.xlabel('Intensity values')
plt.ylabel('Number of pixels')
plt.savefig('Histogramadesiluminado.png',dpi=1200)
plt.show()
'''
while h < 1:
    x=0
    while x< len(ekg):
        if x%2==0:
            ekg.pop(x)
            Tiempo.pop(x)
        x+=1
    print("la longitud de la lista es " + str(len(Tiempo)))
    print("la longitud del vector es " + str(len(ekg)))
    h += 1


tempekg=[]
tempTi=[]
x=0
while x< len(ekg):
    tempekg.append(ekg[x])
    tempTi.append(Tiempo[x])
    x+=1
    if(x>=200):
            tempekg.pop(0)
            tempTi.pop(0)
    drawnow(makeFig)
    '''