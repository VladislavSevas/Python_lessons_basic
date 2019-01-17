
print('Прудников В. В.')

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

print('Задача №1')
import math

spisok = [2, 4, 6, 8, 9, 12, 16, -12, -15, 49, 125, 100]
print('Список изначальный =',spisok)

spisok1 =[]
for spisok in spisok:
    if spisok >= 0:
        sqrt = math.sqrt(spisok)
        if spisok == sqrt ** 2:
            spisok1.append(int(sqrt))
print('Корни из списка =',spisok1)            

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print('Задача №2')

date = {'01':'первое',
        '02':'второе',
        '03':'третье',
        '04':'четвертое',
        '05':'пятое',
        '06':'шестое',
        '07':'седьмое',
        '08':'восьмое',
        '09':'девятое',
        '10':'десятое',
        '11':'одинадцатое',
        '12':'двенадцатое',
        '13':'тринадцатое',
        '14':'четырнадцатое',
        '15':'пятнадцатое',
        '16':'шеснадцатое',
        '17':'семнадцатое',
        '18':'восемнадцатое',
        '19':'девятнадцатое',
        '20':'двадцатое',
        '21':'двадцать первое',
        '22':'двадцать второе',
        '23':'двадцать третье',
        '24':'двадцать четвертое',
        '25':'двадцать пятое',
        '26':'двадцать шестое',
        '27':'двадцать седьмое',
        '28':'двадцать восьмое',
        '29':'двадцать девятое',
        '30':'тридцатое',
        '31':'тридцать первое'}
month = {'01':'января',
         '02':'февраля',
         '03':'марта',
         '04':'апреля',
         '05':'мая',
         '06':'июня',
         '07':'июля',
         '08':'августа',
         '09':'сентября',
         '10':'октября',
         '11':'ноября',
         '12':'декабря'}
datenow = input('Введите дату (дд.мм.гггг): ')

print(f'Дата прописью: {date[datenow[0:2]]} {month[datenow[3:5]]} {datenow[6:10]} года')
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print('Задача №3')

import random
n = int(input('Введи количество символов в списке: '))
i = 0
spisok =[]
while i < n:
    spisok.append(random.randint(-100, 100))
    i += 1
print('Получившийся список =',spisok)    

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print('Задача №4')
list1 = [1, 2, 3, 4, 5, 6, 7, 5, 2, 9, 4]
print('Стартовый список: ',list1)
list2 = set(list1)
print('список без повторений элементов: ', list2)
list3 = []
for x in list1:
    if list1.count(x) == 1:
        list3.append(x)
print('Список уникальных элементов: ',list3)


