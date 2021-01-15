"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# вариант A (через словарь)
# формируем список предыдущих значений
previous_ones = my_list[:-1]
previous_ones[0:0] = [None]

# будем работать со словарем {ключи - наш список: значение - предыдущее значение}
dictionary = dict(zip(my_list, previous_ones))

new_list = [k for (k, v) in dictionary.items() if v and k > v]
print(f"вариант A: {new_list}")


# вариант B (через конструкцию yield)
def generator(a):
    for elem in range(len(a)):
        if elem > 0 and a[elem] > a[elem - 1]:
            yield a[elem]


g = generator(my_list)
new_list = [n for n in g]
print(f"вариант B: {new_list}")
