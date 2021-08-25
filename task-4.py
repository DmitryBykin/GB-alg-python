# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
import random

type = input('введите тип: (1-целое число, 2-вещественное, 3-символ): ')
if type == '1':
    min_value = int(input('Введите минимальное значение: '))
    max_value = int(input('Введите максимальное значение: '))
    if min_value > max_value:
        print('Ошибка. Максимальное значение должно быть больше минимального')
        exit(0)
    rand_value = random.randint(min_value, max_value)
    print(f'Случайное целое число от {min_value} до {max_value}: {rand_value}')
elif type == '2':
    min_value = float(input('Введите минимальное значение: '))
    max_value = float(input('Введите максимальное значение: '))
    if min_value > max_value:
        print('Ошибка. Максимальное значение должно быть больше минимального')
        exit(0)
    rand_value = random.uniform(min_value, max_value)
    print(f'Случайное вещественное число от {min_value} до {max_value}: {rand_value}')
elif type == '3':
    min_char = input('Введите начальный символ: ')
    max_char = input('Введите конечный символ: ')
    if min_char > max_char:
        print('Ошибка. Начальный символ не может быть больше конечного')
        exit(0)
    rand_char = random.randint(ord(min_char), ord(max_char))
    print(f'Случайный символ от {min_char} до {max_char}: {chr(rand_char)}')
else:
    print('Введено неверное значение')
