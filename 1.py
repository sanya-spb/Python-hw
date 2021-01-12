"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("division by zero!")
        return


def input_int(msg="введите число: ", err="ошибка ввода!"):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(err)
            continue


a = input_int("a = ")
b = input_int("b = ")

print(divide(a, b))
