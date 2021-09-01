# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.

firms_count = int(input('Введите количество предприятий: '))
firms = {}
for _ in range(firms_count):
    profit_list = []
    firm_name = input('Название предприятия: ')
    for i in range(1, 5):
        profit = int(input(f'Введите прибыль за {i} квартал: '))
        profit_list.append(profit)
    firms[firm_name] = profit_list

avr_profit_total = 0
for _, profit_list in firms.items():
    for profit in profit_list:
        avr_profit_total += profit
avr_profit_total /= len(firms)
print(f'Средняя прибыль по всем предприятиям: {avr_profit_total}')

for firm_name, profit_list in firms.items():
    avr_profit_cur = 0
    for profit in profit_list:
        avr_profit_cur += profit
    if avr_profit_cur > avr_profit_total:
        print(f'У фирмы {firm_name} прибыль выше среднего')
    elif avr_profit_cur == avr_profit_total:
        print(f'У фирмы {firm_name} прибыль равна среднему значению')
    else:
        print(f'У фирмы {firm_name} прибыль ниже среднего')
