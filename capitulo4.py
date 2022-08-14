
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import random
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
def graficaracum(datos):
    
    plt.figure(1)
    x=range(len(datos))
    plt.bar(x, datos, align='center')
    plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
    plt.title('Cumulative histogram')
    plt.xlabel('Intensity values')
    plt.ylabel('Number of pixels')
    plt.savefig('Histograma_Acumulativo.png',dpi=1200)
    plt.show()
    return None

def graficarEcua(datos):
    
    plt.figure(1)
    x=range(len(datos))
    plt.bar(x, datos, align='center')
    plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
    plt.title('Enhanced histogram')
    plt.xlabel('Intensity values')
    plt.ylabel('Number of pixels')
    plt.savefig('Histograma_Ecualizado.png',dpi=1200)
    plt.show()
    return None
#IMAGEN 1
Imagen='52.jpg'
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
'''

#1 procesamiento
#Este for sirve para aumentar o disminuir el brillo mediante la multipliacaion de la informaicon de los pixels
# for x in range(len(IC)):
for x in range(len(ig)):
    for h in range(len(ig[x])):
            ig[x][h]=ig[x][h]*1.5
            if ig[x][h]>=256: 
                ig[x][h]=255
plt.imshow(ig,cmap='gray')
plt.axis('off')
plt.savefig('Conaum.png',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.title('Imagen con el contraste aumentado')
plt.show()
for x in range(len(ig)):
    for h in range(len(ig[x])):
            ig[x][h]=ig[x][h]+10
            if ig[x][h]>=256: 
                ig[x][h]=255
plt.imshow(ig,cmap='gray')
plt.axis('off')
plt.savefig('Brillo.png',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.title('Imagen con el brillo aumentado')
plt.show()

#ACCEDER AL RGB
for x in range(len(I)):
    for h in range(len(I[x])):
        for f in range(len(I[x][h])):
            I[x][h][f]=I[x][h][0]
            if I[x][h][f]>=255: 
                I[x][h][f]=254
plt.imshow(I)
plt.title("RGB 0")
plt.show()
'''

#2 procesamiento            
rgb = [0.2989, 0.5870, 0.1140]
ig = np.dot(I[...,:3], rgb)
IC=255-ig
plt.imshow(IC,cmap='gray')
plt.axis('off')
plt.savefig('comp.png',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.title('Imagen complemento')
plt.show()

#1 Primer histograma
from PIL import Image
foto=Image.open('C:\\Users\\brian.cobian\\Desktop\\Scripts\\' + Imagen)
#si la imagen es a color la convertimos a escala de grises
if foto.mode != 'L':
    foto=foto.convert('L')
histograma=foto.histogram()
graficar(histograma)


"""
#3 procesamiento segmentacion  
h1=[]
h2=[] 
for x in range(len(ig)):
    for h in range(len(ig[x])):
            h1.append(ig[x][h])
            if ig[x][h]<80: 
                ig[x][h]=0
            else:
                ig[x][h]=1
            h2.append(ig[x][h])
plt.imshow(ig,cmap='gray')
plt.axis('off')
plt.savefig('segmentacion.png',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.title("Segmentacion por umbral")
plt.savefig('temp', bbox_inches='tight')
plt.show()
foto=Image.open('C:\\Users\\brian.cobian\\Desktop\\Scripts\\temp.png')
#si la imagen es a color la convertimos a escala de grises
if foto.mode != 'L':
    foto=foto.convert('L')
histograma=foto.histogram()
graficar(histograma)
"""


#Histograma acumulativo
#carga la imagen directamente a escala de grises
foto=Image.open('C:\\Users\\brian.cobian\\Desktop\\Scripts\\' + Imagen).convert('L')
histograma=foto.histogram()
foto.close()
h_acumulativo=[]
sumatoria=0
#funcion del histograma acumulativo
for valor in histograma:
    sumatoria+=valor
    h_acumulativo.append(sumatoria)
graficaracum(h_acumulativo)
"""
#4 procesamiento   "Contraste automatico"
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
            r1 = random.randint(1, 150)
            ig[x][h]=(ig[x][h]*-1) 
            AC.append((ig[x][h]+ r1)/4)
plt.imshow(ig,cmap='gray')
plt.axis('off')
plt.savefig('ConAuto.png',dpi=1200)
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
"""
#Histograma acumulativo
#carga la imagen directamente a escala de grises
foto=Image.open('C:\\Users\\brian.cobian\\Desktop\\Scripts\\' + Imagen).convert('L')
datos=foto.getdata()
#ecualizacion lineal
datos_lineales=[]
h_w=foto.height*foto.width
auxiliar=255/h_w
for x in datos:
    datos_lineales.append(round(h_acumulativo[x]*auxiliar))
foto_ecualizada=Image.new('L',foto.size)
foto_ecualizada.putdata(datos_lineales)
foto_ecualizada.save('C:\\Users\\brian.cobian\\Desktop\\Scripts\\temp.png')
foto.close()
foto_ecualizada.close()
foto=Image.open('C:\\Users\\brian.cobian\\Desktop\\Scripts\\temp.png')
if foto.mode != 'L':
    foto=foto.convert('L')
plt.imshow(foto,cmap='gray')
plt.axis('off')
plt.savefig('Ecualizada.png',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.title('Imagen ecualizada')
plt.show()
histograma=foto.histogram()
graficar(histograma)
foto.close()
h_acumulativo=[]
sumatoria=0
#funcion del histograma acumulativo
for valor in histograma:
    sumatoria+=valor
    h_acumulativo.append(sumatoria)
graficarEcua(h_acumulativo)


