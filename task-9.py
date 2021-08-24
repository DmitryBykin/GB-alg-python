# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = [[1, 2, 3], [4, 5, 6], [7, 0, 9], [3, 6, 7]]
min_by_col_values = []


def get_min_elem_value(nums_list):
    if len(nums_list):
        min_value = nums_list[0]
        for elem in nums_list:
            if elem < min_value:
                min_value = elem
        return min_value
    else:
        print('Список пустой')
        return None


def get_max_elem(nums_list):
    if len(nums_list):
        max_value = nums_list[0]
        for elem in nums_list:
            if elem > max_value:
                max_value = elem
        return max_value
    else:
        print('Список пустой')
        return None


for col in range(len(matrix[0])):
    col_nums = []
    for row in range(len(matrix)):
        col_nums.append(matrix[row][col])
    min_by_col_values.append(get_min_elem_value(col_nums))

print('Матрица:')
for row in matrix:
    print(row)

max_value = get_max_elem(min_by_col_values)
print(f'Максимальный элемент матрицы из минимальных элементов столбцов: {max_value}')
