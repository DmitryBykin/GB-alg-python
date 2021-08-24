# 4. Определить, какое число в массиве встречается чаще всего.


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


nums_list = [1, 2, 3, 4, 4, 4, 7, 8, 4, 9, 0]
count_values_list = []
for elem in nums_list:
    cur_elem = elem
    cur_elem_count = 0
    for elem in nums_list:
        if cur_elem == elem:
            cur_elem_count += 1
    count_values_list.append(cur_elem_count)

max_ind = get_max_elem_ind(count_values_list)
print(f'Число, которое встречается максимальное число раз - {nums_list[max_ind]}')
