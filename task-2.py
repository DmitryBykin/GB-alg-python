# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Введите число: ')
odd_count, even_count = 0, 0

for digit in num:
    if int(digit) % 2 == 1:
        odd_count += 1
    else:
        even_count += 1

print(f'Нечетных цифр - {odd_count}, четных - {even_count}')
