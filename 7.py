"""

"""

int_func = lambda text: str(text).capitalize()


def my_func(text):
    tmp_list = str(text).split(' ')
    result = []
    for world in tmp_list:
        result.append(int_func(world))
    return result


print(*my_func(input("строка из слов, разделённых пробелом: ")))
