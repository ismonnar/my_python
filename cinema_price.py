def sale1(a, b):
    if b == 'завтра':
        return float(a*0.95)
    else:
        return a

def sale2(a, b):
    if b>=20:
        return float(a*0.8)
    else:
        return a

film = input('Выбрать фильм: ')
day = input('Выбрать день (сегодня, завтра): ')
time = int(input('Выбрать время: '))
tickets = int(input('Выбрать количество билетов: '))
print('Выбрали фильм: ', film, 'День: ', day, 'Время: ', time, 'Количество билетов: ', tickets)

if film == 'Пятница':
    if time == 12:
        print(sale1(sale2(250*tickets, tickets), day))
    elif time == 16:
        print(sale1(sale2(350*tickets, tickets), day))
    elif time == 20:
        print(sale1(sale2(450*tickets, tickets), day))
    else:
        print('В данное время сеансов нет')
elif film == 'Чемпионы':
    if time == 10:
        print(sale1(sale2(250*tickets, tickets), day))
    elif time == 13:
        print(sale1(sale2(350*tickets, tickets), day))
    elif time == 16:
        print(sale1(sale2(350*tickets, tickets), day))
    else:
        print('В данное время сеансов нет')
elif film == 'Пернатая банда':
    if time == 10:
        print(sale1(sale2(350*tickets, tickets), day))
    elif time == 14:
        print(sale1(sale2(450*tickets, tickets), day))
    elif time == 18:
        print(sale1(sale2(450*tickets, tickets), day))
    else:
        print('В данное время сеансов нет')
else:
    print('Данного фильма нет в списке сеансов')
