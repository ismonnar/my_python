lines_list = open('temper.txt').read().splitlines()
my_list = [float(i) for i in lines_list]
print('Максимальная температура:', max(my_list))
print('Минимальная температура:', min(my_list))
print('Количество уникальных температур:', len(list(set(my_list))))
print('Средняя температура:', sum(my_list)/len(my_list))
