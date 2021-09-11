# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib


def compare_str(str1, str2):
    s1 = hashlib.sha1(str1).hexdigest()
    s2 = hashlib.sha1(str2).hexdigest()
    return s1 == s2


def get_count_substr(source_str, substr):
    source_str_length = len(source_str)
    find_substr_length = len(substr)
    count = 0
    for i in range(source_str_length - find_substr_length + 1):
        if compare_str(substr.encode(), source_str[i:i + find_substr_length].encode()):
            count += 1
    return count


matches = {}
input_str = 'hello python world, python language'
for i in range(len(input_str)):
    for j in range(i + 1, len(input_str) + 1):
        cur_substr = input_str[i:j]
        if ' ' in cur_substr:  # "рваные" подстроки с пробелами не учитываем
            continue
        res = get_count_substr(input_str, cur_substr)
        if res:
            try:
                matches[cur_substr] += 1
            except KeyError:
                matches[cur_substr] = 1

for key, val in matches.items():
    print(key, val)
print(f'Всего различных подстрок в строке "{input_str}": {len(matches.values())}')
