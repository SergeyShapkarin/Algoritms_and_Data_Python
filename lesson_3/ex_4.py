'''4. Определить, какое число в массиве встречается чаще всего.'''

from random import randint


first_list = [randint(0, 5) for __ in range(30)]

max_count = 0
item = ''

for i in set(first_list):
    if first_list.count(i) > max_count:
        item = str(i)
        max_count = first_list.count(i)
    elif first_list.count(i) == max_count:
        item += ', '+str(i)

print(f'Исходный массив элементов {first_list}')
if len(item.split(',')) > 1:
    print(f'Числа {item} встречаются в массиве {max_count} раз(а)')
else:
    print(f'Число {item} встречается в массиве {max_count} раз(а)')



