# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они
# стоят и сколько между ними находится букв.

# алфавит латинский a-z

letter_first = input('Введите первую букву: ')
letter_second = input('Введите вторую букву: ')

start_ascii_position = ord(letter_first)
position_first = ord(letter_first) - start_ascii_position + 1  # считаем с 1
position_second = ord(letter_second) - start_ascii_position + 1
between_letters = position_second - position_first - 1
print(f'Позиция первой буквы в алфавите: {position_first}')
print(f'Позиция второй буквы в алфавите: {position_second}')
print(f'Между ними {between_letters} букв(ы)')
