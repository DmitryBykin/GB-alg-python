# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и
# отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

from random import randrange


def sort_bubble(data_list):
    n = 1
    length_data_list = len(data_list)
    while n < length_data_list:
        for i in range(length_data_list - n):
            if data_list[i] < data_list[i + 1]:
                data_list[i], data_list[i + 1] = data_list[i + 1], data_list[i]
        n += 1
    return data_list


input_list = [randrange(-100, 100) for _ in range(10)]
print(f'Исходный список: {input_list}')
sorted_list = sort_bubble(input_list)
print(f'Отсортированный (по убыванию) список: {sorted_list}')
