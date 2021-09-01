# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

DEC_TO_HEX = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
              15: 'F'}
HEX_TO_DEC = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
              'D': 13, 'E': 14, 'F': 15}


def from_hex_to_dec(hex_value):
    length = len(hex_value)
    result = 0
    for i in range(length):
        result += HEX_TO_DEC[hex_value[i]] * (16 ** (length - 1 - i))
    return result


def from_dec_to_hex(dec_value):
    result = deque()
    cur_value = dec_value
    while cur_value > 0:
        cur_rest = cur_value % 16
        cur_value = cur_value // 16
        result.appendleft(DEC_TO_HEX[cur_rest])
    return result


def deque_to_str(num):
    res = ''
    for dig in num:
        res += dig
    return res


num_1 = input('Введите первое HEX число: ').upper()
num_2 = input('Введите второе HEX число: ').upper()

num_1 = deque(num_1)
num_2 = deque(num_2)

if len(num_1) > len(num_2):
    for _ in range(len(num_1) - len(num_2)):
        num_2.appendleft('0')
else:
    for _ in range(len(num_2) - len(num_1)):
        num_1.appendleft('0')

result = deque()
transfer = 0
for i in range(len(num_1) - 1, -1, -1):
    sum = HEX_TO_DEC[num_1[i]] + HEX_TO_DEC[num_2[i]] + transfer
    transfer = sum // 16
    sum %= 16
    result.appendleft(DEC_TO_HEX[sum])
print(f'Сумма чисел {deque_to_str(num_1)} и {deque_to_str(num_2)} = {deque_to_str(result)}')

multiply_dec = from_hex_to_dec(num_1) * from_hex_to_dec(num_2)
multiply_hex = from_dec_to_hex(multiply_dec)

print(f'Произведение чисел {deque_to_str(num_1)} и {deque_to_str(num_2)} = {deque_to_str(multiply_hex)}')
