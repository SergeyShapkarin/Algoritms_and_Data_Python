'''4. Пользователь вводит две буквы. Определить, на каких местах алфавита
они стоят, и сколько между ними находится букв.'''

try:
    a, b = input('Введите две буквы через запятую: ').split(',')
    a = a.strip().lower()
    b = b.strip().lower()
except:
    print('Введены некорректные значения')
else:
    if len(a) == 1 and a.isalpha() and len(b) == 1 and b.isalpha():
        if ord(a) in range (97, 123) and ord(b) in range (97, 123):
            print(f'Номер буквы {a} в алфивите {abs(96 - ord(a))}')
            print(f'Номер буквы {b} в алфивите {abs(96 - ord(b))}')
        elif ord(a) in range (1072, 1104) and ord(b) in range (1072, 1104):
            print(f'Номер буквы {a} в алфивите {abs(1071 - ord(a))}')
            print(f'Номер буквы {b} в алфивите {abs(1071 - ord(b))}')
        else:
            print('Введены символы неизвестного нам алфавита')

        if a == b:
            print('Введена одна буква дважды')
        elif (ord(b) - ord(a)) == 1:
            print('Введены два соседних символа')
        else:
            print(f'Между {a} и {b} - {abs(ord(b) - ord(a)) - 1} символов')
    else:
        print('Введены некорректные значения')
