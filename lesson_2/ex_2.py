'''2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2
нечетные (3 и 5).'''

number = input('Введите натуральное число:  ')
odd = 0
even = 0

for i in number:
    if ( int(i) % 2 ) == 1:
        odd += 1
    else:
        even += 1

print(f'Четных:   {even}\nНечетных: {odd}')