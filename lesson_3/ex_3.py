'''3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы.'''

from random import randint


first_list = [randint(0, 100) for __ in range(15)]

def revers_min_max(list):
    min = list[0]
    max = list[0]
    for i in list:
        if i < min:
            min = i
        if i > max:
            max = i
    spam = list.index(min)
    egg = list.index(max)
    list[spam], list[egg] = max, min
    return list

print(f'Исходный массив элементов {first_list}')
print(f'Измененный массив елементов {revers_min_max(first_list)}')