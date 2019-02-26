from math import sin

def mysin(x):
    if 0.2 <= x <= 0.9:
        return sin(x)
    else:
        return 1
    
x = float(input('Введите число: '))
print(mysin(x))
