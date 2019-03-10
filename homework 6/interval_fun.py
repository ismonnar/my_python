def y(x):
    return x**2+3

total=0
for i in range(10,32,2):
    total+=y(i)

print(total)
