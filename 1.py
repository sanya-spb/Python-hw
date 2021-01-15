"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

try:
    py_name, productivity, rate, bonus = argv
    productivity, rate, bonus = float(productivity), float(rate), float(bonus)
except ValueError:
    print("необходимо запускать скрипт с числовыми параметрами")
    exit()

print(f"(выработка в часах*ставка в час) + премия = {productivity * rate + bonus}")
