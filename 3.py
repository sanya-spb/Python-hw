# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

import re

count = 0
sum = 0

print("Сотрудники, имеющие оклад менее 20 тыс.:")
try:
    with open("3.txt", encoding="utf-8") as f_obj:
        for line in f_obj:
            filtered_data = re.split("\s+", line)
            employee, salary = filtered_data[0], float(filtered_data[1])
            count += 1
            sum += salary
            if salary < 20000:
                # по формату
                # print(f"{employee}: {salary}")
                # или с исходника
                print(f"{line}", end="")
except IOError:
    print("IOError!")
except ValueError:
    print(f"Input format Error: {line}")
    exit(1)

print(f"Средняя величина дохода сотрудников: { round((sum / count), 2)}")
