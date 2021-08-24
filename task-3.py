# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

MAX_VALUE = 10


def get_max_elem_ind(nums_list):
    if len(nums_list):
        max_value = nums_list[0]
        max_value_ind = 0
        for ind, elem in enumerate(nums_list):
            if elem > max_value:
                max_value = elem
                max_value_ind = ind
        return max_value_ind
    else:
        print('Список пустой')
        return None


def get_min_elem_ind(nums_list):
    if len(nums_list):
        min_value = nums_list[0]
        min_value_ind = 0
        for ind, elem in enumerate(nums_list):
            if elem < min_value:
                min_value = elem
                min_value_ind = ind
        return min_value_ind
    else:
        print('Список пустой')
        return None


nums_count = int(input('Введите количество элементов: '))
random_list = [random.randint(0, MAX_VALUE) for _ in range(nums_count)]
print(f'Исходный список: {random_list}')
min_ind = get_min_elem_ind(random_list)
max_ind = get_max_elem_ind(random_list)
random_list[min_ind], random_list[max_ind] = random_list[max_ind], random_list[min_ind]
print(f'Преобразованный список: {random_list}')
