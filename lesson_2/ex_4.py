'''4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
 Количество элементов (n) вводится с клавиатуры.'''

n = int(input('Введите количество элементов:  '))


def divizion(n, m=1):
    if n == 1:
        return m
    else:
        m = m + divizion(n-1, m/-2)
        return m


print(divizion(n))