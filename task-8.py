# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
# в последнюю ячейку строки. В конце следует вывести полученную матрицу.

ROWS = 5
COLS = 4
matrix = []

for row in range(ROWS):
    cur_row = []
    cur_row_elems_sum = 0
    for col in range(COLS - 1):
        cur_matrix_elem = int(input(f'Введите ({row},{col}) элемент матрицы: '))
        cur_row.append(cur_matrix_elem)
        cur_row_elems_sum += cur_matrix_elem
    cur_row.append(cur_row_elems_sum)
    matrix.append(cur_row)

for row in matrix:
    print(row)
