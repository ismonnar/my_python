from random import randint
x=[]
for i in range(1000):
    x.append(randint(-10,10))

mi = x.index(min(x))
ma = x.index(max(x))
print(mi)
print(ma)

c=0
if mi<ma:
    for i in range(mi,ma):
        if x[i]<0:
            c=c+1
else:
    for i in range(ma,mi):
        if x[i]<0:
            c=c+1

print(c)
