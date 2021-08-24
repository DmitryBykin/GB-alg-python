# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться

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


nums_list = [1, 2, 3, 4, 0, 4, 3, 5, 6, 9, 6]

min_elem_ind = get_min_elem_ind(nums_list)
first_min_value = nums_list[min_elem_ind]

nums_list.pop(min_elem_ind)
min_elem_ind = get_min_elem_ind(nums_list)
second_min_value = nums_list[min_elem_ind]

print(f'Минимальные элементы списка: {first_min_value} и {second_min_value} ')
