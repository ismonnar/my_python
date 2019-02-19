def fun1(a):
    if -2.4<=a<=5.7:
        return a**2
    else:
        return 4.0

num = float(input('Введите число: '))
print(fun1(num))
