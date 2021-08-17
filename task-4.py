# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

elem_count = int(input('Введите количество элементов: '))
divider = -2
sum = 0
cur_elem = 1
for _ in range(elem_count):
    sum += cur_elem
    cur_elem = cur_elem / divider

print(f'Сумма ряда: {sum}')
