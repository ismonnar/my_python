numsum=0
while True:
    num=input('Введите число/"стоп" (для выхода): ')
    if not num.isdigit():
        if num.lower()=='стоп':
            print(numsum)
            break
        else:
            print('Ошибка ввода')
    else:
        numsum += int(num)
