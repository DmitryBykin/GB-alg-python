# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# 5-ая задача из 3-го урока.
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение.
# примечание - в исходной задаче убрал требование по поиску индекса - выводится только сам элемент

import timeit

setup_code = '''
import random

n = 10000
max_num = 10
min_num = -10
nums_list = [random.randint(min_num, max_num) for x in range(n)]
'''

# первый способ

code_1 = '''
def get_max_negative_elem(nums_list):
    if len(nums_list):
        find_element = False
        for elem in nums_list:
            if elem < 0:
                max_negative_elem = elem
                find_element = True

        for elem in nums_list:
            if elem < 0 and elem > max_negative_elem:
                max_negative_elem = elem

        if find_element:
            return max_negative_elem
        else:
            print('В списке нет ни одного отрицательного числа')
            return None
    else:
        print('Список пустой')
        return None

max_negative_elem = get_max_negative_elem(nums_list)
# print(f'Максимальный отрицательный элемент в списке: {max_negative_elem}')
'''

print(timeit.timeit(code_1, setup_code, number=10))


# второй способ - из списка выбрать все отрицательные элементы, затем отсортировать список по возрастанию и
# взять последний элемент

code_2 = '''
negative_list = []
for elem in nums_list:
    if elem < 0:
        negative_list.append(elem)
negative_list.sort()
max_negative_elem = negative_list[-1]
# print(f'Максимальный отрицательный элемент в списке: {max_negative_elem}')
'''

print(timeit.timeit(code_2, setup_code, number=10))

# сложность первого способа - O(n), затраченное время - 0.0083 сек (при n=10000)
# сложность второго способа = сложности функции sort = O(n * log n), затраченное время - 0.0086 сек. (при n=10000)
# при n>10000 второй алгоритм немного медленнее
