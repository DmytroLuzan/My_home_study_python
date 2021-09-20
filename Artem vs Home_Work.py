"""
Через цикли while  і for
1. Вивести значення від 1 до 10 включно з кроком 1
2. Вивести список з значеннями від 1 до 10 з кроком 1
"""


def num_range(start, stop, step):
    list1 = []
    while start < stop:
        list1.append(start)
        start += step
    print(list1)
    return list1


num_range(1, 11, 1)
