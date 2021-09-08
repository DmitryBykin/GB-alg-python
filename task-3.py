# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

import numpy as np
from random import randint

M = 5


def find_median(input_list):
    for i in range(len(input_list)):
        left_part_count, right_part_count = 0, 0
        for j in range(len(input_list)):
            if i == j:
                continue
            if input_list[i] > input_list[j]:
                right_part_count += 1
            if input_list[i] < input_list[j]:
                left_part_count += 1
        if right_part_count == left_part_count:
            return input_list[i]


input_list = []
i = 0
while i < 2 * M + 1:
    rand_num = randint(-10, 10)
    if rand_num not in input_list:  # считаем, что элементы не повторяются
        input_list.append(rand_num)
        i += 1

print(sorted(input_list))  # сортируем для удобства проверки
print(f'Медиана, найденная с помощью функции "find_median": {find_median(input_list)}')
print(f'Медиана, найденная с помощью библиотеки numpy: {np.median(input_list)}')
