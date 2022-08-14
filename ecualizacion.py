
import matplotlib.pyplot as plt
from PIL import Image

def histeq(photo,cumulative,data):
    Linear_data=[]
    h_w=photo.height*photo.width
    auxiliar=255/h_w
    for x in data:
        Linear_data.append(round(cumulative[x]*auxiliar))
    Photo_equalized =Image.new('L',photo.size)
    Photo_equalized .putdata(Linear_data)
    Photo_equalized .save('C:\\Users\\brian.cobian\\Desktop\\Scripts\\temp.png')
    photo.close()
    return Photo_equalized 
Picture='52.jpg'
photo=Image.open('C:\\Users\\brian.cobian\\Desktop\\Scripts\\' + Picture).convert('L')
data=photo.getdata()
histogram=photo.histogram()
photo.close()
h_cumulative=[]
summation=0
for valor in histogram:
    summation+=valor
    h_cumulative.append(summation)

Photo_ecualized=histeq(photo,h_cumulative,data)
plt.imshow(Photo_ecualized,cmap='gray')
plt.axis('off')
plt.savefig('Ecualizada.png',bbox_inches='tight',pad_inches=0,dpi=1200)
plt.title('Imagen ecualizada')
plt.show()
Photo_ecualized.close()




#funcion del histograma acumulativo





