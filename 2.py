"""
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
"""


def process_data(fname=None, lname=None, born=None, city=None, email=None, phone=None):
    print(f"данные пользователя: {fname}, {lname}, {born}, {city}, {email}, {phone}")


user_data = {}
process_data(
    fname=input("имя: "),
    lname=input("фамилия: "),
    born=input("год рождения: "),
    city=input("город проживания: "),
    email=input("email: "),
    phone=input("телефон: ")
)
