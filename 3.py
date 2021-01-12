"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    tmp_list = list([a, b, c])
    tmp_list.sort()
    return tmp_list[-1] + tmp_list[-2]


def input_int(msg="введите число: ", err="ошибка ввода!"):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(err)
            continue


a = input_int("a = ")
b = input_int("b = ")
c = input_int("c = ")

print(my_func(a, b, c))
