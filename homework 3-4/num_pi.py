from math import pi

def mypi(x):
    return f'{pi:.{x}f}'

x = int(input('Введите количество знаков числа Пи после запятой: '))
print(mypi(x))
