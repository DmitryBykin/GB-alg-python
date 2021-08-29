# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
#
#     Без использования «Решета Эратосфена»;
#     Используя алгоритм «Решето Эратосфена»
#
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
import timeit

# без использования решета Эратосфена

code_1 = '''
n = 1000


def prime(n):
    for i in range(2, n): # можно использовать n/2, оставил n, чтобы расчёт был дольше
        if n % i == 0:
            return False
    return True


cur_num = 2
i = 1 # нумерация с 1
while True:
    if prime(cur_num):
        if i == n:
            print(f'i-ое (i={i}) простое число: {cur_num}')
            break
        i += 1
    cur_num += 1
'''

# с использованием решета Эратосфена

code_2 = '''
n = 1000

def get_resheto_i_elem(n, i):
    sieve = set(range(2, n + 1))
    cur_prime_elem_num = 1
    while sieve:
        prime = min(sieve)
        if cur_prime_elem_num == i:
            return prime
        cur_prime_elem_num += 1
        sieve -= set(range(prime, n + 1, prime))


import math


def prime_counting_function(i):    
    number_of_primes = 1
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


res = get_resheto_i_elem(prime_counting_function(n), n)
print(f'i-ое (i={n}) простое число (с использованием решета Эратосфена): {res}')
'''

print(timeit.timeit(code_1, number=10))
print(timeit.timeit(code_2, number=10))

# сложность первого способа - O(n^2), затраченное время - 2.11 сек (для поиска i=10000 простого числа)
# сложность второго способа (решето Эратосфена) - O(n * log log n), затраченное время - 0.25 сек. (для поиска i=10000 простого числа)
# второй алгоритм работает быстрее
