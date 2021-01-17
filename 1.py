# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

try:
    with open("1.out", "w", encoding="utf-8") as f_obj:
        while True:
            s = input("Enter something to file (Enter for exit): ")
            if not s:
                break
            print(s, file=f_obj)
except IOError:
    print("IOError!")
