# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

import re

try:
    with open("2.txt", encoding="utf-8") as f_obj:
        file = f_obj.readlines()
except IOError:
    print("IOError!")

print(f"Amount lines: {len(file)}")
for line, value in enumerate(file):
    # нет точного определения что такое "слово" в постановке задачи:
    #
    # a) если словом мы считаем все что разделено пробелом/пробелами
    # worlds = re.findall("\S+", value)
    #
    # b) если словом мы считаем буквы и цифры, разделенные пробелами, знаками препинания, скобками и др. знаками
    # worlds = re.findall("\w+", value)
    #
    # c) ну или перечислим все возможные разделители слов (сорян, люблю регулярки)
    worlds = re.findall("[^\s\.\,!:/#\\\)\(\^\+\"'=\{\}\[\]]+", value)
    print(f"line {line + 1}: worlds: {len(worlds)} {worlds}")
