# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.

import json
from statistics import mean

try:
    with open("7.txt", encoding="utf-8") as f_obj:
        my_dict = {name: int(proceeds) - int(costs) for (name, ownership, proceeds, costs) in
                   [[x for x in line.split()] for line in f_obj]}
except IOError:
    print("IOError!")
except ValueError:
    print("File data error!")
    exit(1)

# mean - вычисление среднего значения (из модуля statistics)
result = [my_dict, {"average_profit": round(mean(list(filter(lambda x: x > 0, list(my_dict.values())))), 2)}]

try:
    with open("7.json", "w", encoding="utf-8") as f_obj:
        json.dump(result, f_obj)
except IOError:
    print("IOError!")
