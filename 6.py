"""
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""

# вариант а
# def int_func(text):
#    return str(text).capitalize()

# вариант b
int_func = lambda text: str(text).capitalize()

print(int_func(input("введите слово: ")))
