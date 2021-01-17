# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

rnd_min, rnd_max, count = 0, 9, 5

print("Генерируем набор данных в файл..")
try:
    with open("5.out", "w", encoding="utf-8") as f_obj:
        print(
            ' '.join(
                [str(rnd) for rnd in [random.randint(rnd_min, rnd_max) for _ in range(count)]]
            ), file=f_obj
        )
except IOError:
    print("IOError!")

# читаем
try:
    with open("5.out", encoding="utf-8") as f_obj:
        array = [int(x) for x in f_obj.readline().split()]
except IOError:
    print("IOError!")
except ValueError:
    print("File data error!")
    exit(1)

# считаем и выводим результат
print(f"sum({array}) = {sum(array)}")
