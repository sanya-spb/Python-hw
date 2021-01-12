"""
Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения числа в степень
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_power_v1(x, y):
    return x ** y


def my_power_v2(x, y):
    result = 1
    while y < 0:
        result *= x
        y += 1
    return 1 / result


def input_int(msg="введите число: ", err="ошибка ввода!"):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(err)
            continue


def input_float(msg="введите число: ", err="ошибка ввода!"):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(err)
            continue


while True:
    x = input_float("действительное положительное число x: ")
    if x >= 0:
        break

while True:
    y = input_int("целое отрицательное число y: ")
    if y < 0:
        break

print(f"первый способ: {my_power_v1(x, y)}")
print(f"второй способ: {my_power_v2(x, y)}")
