
h1=[102,413,524,23,12,142,45,65,553,64,263,177,288,5]
print(h1)
i=1
for x in range(len(h1)):
    if h1[x-i] <= 60:
        print(h1[x-i])
        h1.pop(x-i)
        i +=1
print(h1)

h1=[0,0,0,0,0,0,53,23,4,2,3,5,34,2,5]
print(h1)
h1.remove(0)
print(h1)
