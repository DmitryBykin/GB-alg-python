# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

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


nums_list = [1, 2, 3, 4, 0, 3, 4, 5, 6, 9, 6]

min_elem_ind = get_min_elem_ind(nums_list)
max_elem_ind = get_max_elem_ind(nums_list)

sum = 0
for i in range(min_elem_ind + 1, max_elem_ind):
    sum +=nums_list[i]

print(f'Список: {nums_list}')
print(f'Сумма элементов списка между элементами {nums_list[min_elem_ind]} и {nums_list[max_elem_ind]}: {sum}')
