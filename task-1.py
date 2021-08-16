# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

while True:
    num = input('Введите 3-х значное число: ')
    if len(num) != 3:
        print('Число должно быть 3-х значным')
        continue
    else:
        break

sum, mul = 0, 1
for char in num:
    sum += int(char)
    mul *= int(char)
print(f'Сумма чисел = {sum}')
print(f'Произведение чисел = {mul}')
