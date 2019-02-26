def stringnum(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s.lower()

s = input('Введите строку: ')
n = int(input('Введите число: '))
print(stringnum(s, n))
