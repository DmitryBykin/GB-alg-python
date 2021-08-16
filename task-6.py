# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# алфавит латинский a-z

letter_num = int(input('Введите номер буквы в алфавите: '))
start_ascii_position = ord('a')
letter_alphabet = chr(start_ascii_position + letter_num - 1)
print(f'Буква в алфавите на позиции {letter_num}: {letter_alphabet}')

