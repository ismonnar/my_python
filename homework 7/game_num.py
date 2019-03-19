import random
tries = 3
number = random.randint(0,9)
print('Компьютер загадал число.')
print('У вас есть', tries, 'попытки. Удачи!')
count=0

while True:
    guess = int(input('Попробуйте угадать: '))

    if number == guess:
        print('Победа!')
        break
    else:
        count=count+1
        if count<tries:
            if number>guess:
                print('Попробуйте число больше!')
            else:
                print('Попробуйте число меньше!')
        else:
            print('Game over!')
            print('Число:',number)
