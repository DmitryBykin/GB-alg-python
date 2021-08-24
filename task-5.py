# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

def get_max_negative_elem_ind(nums_list):
    if len(nums_list):
        find_element = False
        for ind, elem in enumerate(nums_list):
            if elem < 0:
                max_negative_elem = elem
                max_negative_elem_ind = ind
                find_element = True

        for ind, elem in enumerate(nums_list):
            if elem < 0 and elem > max_negative_elem:
                max_negative_elem = elem
                max_negative_elem_ind = ind

        if find_element:
            return max_negative_elem_ind
        else:
            print('В списке нет ни одного отрицательного числа')
            return None
    else:
        print('Список пустой')
        return None


nums_list = [1, -2, 3, 4, 5, -8, 0, -1, 9]
max_ind = get_max_negative_elem_ind(nums_list)
if max_ind != None:
    print(f'Максимальный отрицательный элемент в списке: {nums_list[max_ind]}, его индекс: {max_ind}')
