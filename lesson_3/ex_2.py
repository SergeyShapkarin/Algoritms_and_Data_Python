'''2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо
заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
т. к. именно в этих позициях первого массива стоят четные числа.'''
from random import randint


first_list = [randint(0, 100) for __ in range(50)]

def find_even(list):
    even_elements = []
    for i in list[::]:
        if i % 2 == 0:
            even_elements.append(list.index(i))
            list[list.index(i)] = None
    return even_elements

print(f'Исходный массив элементов {first_list}')
print(f'Четные элементы находятся на индексах {find_even(first_list[::])}')
