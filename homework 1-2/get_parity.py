def parity(a):
    if a//2:
        return 'Чётное'
    else:
        return 'Нечётное'

num = int(input('Введите число: '))
print(parity(num))
