number = input("Введите число: ")
digits = [int(k)**2 for k in number if int(k)%2!=0]
print(sum(digits))
