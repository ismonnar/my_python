from random import randint

number = randint(1, 4)
answer = int(input('Угадайте число: '))
if answer == number:
    print('Победа!')
else:
    print('Давай по новой, Миша.')
    if answer > number:
        print('Число было меньше')
    else:
        print('Число было больше')
