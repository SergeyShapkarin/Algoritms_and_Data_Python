'''5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный»
и «максимальный отрицательный». Это два абсолютно разных значения.'''

from random import randint


first_list = [randint(-100, 100) for __ in range(30)]
max = None

for i in [e for e in first_list if e < 0]:
    if max == None:
        max = i
    elif abs(i) < abs(max):
        max = i

print(first_list)
print(f'Максимальный отрицательный элемент массива равен {max}, расположен на '
      f'позиции {first_list.index(max)}')