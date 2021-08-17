# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num_count = int(input('Введите количество чисел: '))
max_sum, max_num = 0, 0
for i in range(num_count):
    num = input(f'Введите число {i + 1}: ')
    sum_char = 0
    for char in num:
        sum_char += int(char)
    if sum_char > max_sum:
        max_sum = sum_char
        max_num = num

print(f'Число с максимальной суммой цифр: {max_num}. Сумма цифр: {max_sum}')
