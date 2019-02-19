def max(a, b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return 'Числа равны'

num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))
print(max(num1, num2))

