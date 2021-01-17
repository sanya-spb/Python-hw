# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

dictionary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре'
}

try:
    with \
            open("4.txt", encoding="utf-8") as f_input, \
            open("4.out", "w", encoding="utf-8") as f_output:
        for line in f_input:
            print(
                ' '.join(
                    [dictionary.get(word.lower(), word).capitalize() for word in line.split()]
                ), file=f_output
            )
except IOError:
    print("IOError!")
