number = input("Введите номер элемента: ")
if number:
    intnum = int(number)
    if intnum == 3:
        print('Li')
    elif intnum == 25:
        print('Mn')
    elif intnum == 80:
        print('Hg')
    elif intnum == 17:
        print('Cl')
    else:
        print('Что это?')
else:
    print('Введите номер элемента!')
