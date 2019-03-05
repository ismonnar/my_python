import random
L=['самовар','весна','лето']
n = random.choice(L)
print('Выбираем случайное слово: ',n)
i= random.randint(0,len(n)-1)
print('Выбираем случайную букву: ',n[i])
j = n[:i] + '?' + n[i+1:]

print(j)
while True:
    s=input('Введите букву: ')
    if n[i]==s:
        print('Победа!')
        break
    else:
        print('Попробуйте ещё раз!')
print('Слово: ' + n)
