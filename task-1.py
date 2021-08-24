# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

aliquot_counts = [0 for x in range(10)]
for num in range(2, 100):
    for aliquot_num in range(2, 10):
        if num % aliquot_num == 0:
            aliquot_counts[aliquot_num] += 1

for i in range(2, 10):
    print(f'Чисел кратных {i} - {aliquot_counts[i]}')
