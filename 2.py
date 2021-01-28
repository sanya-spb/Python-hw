"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self) -> str:
        return self._msg


while True:
    d = input("на что будем делить 100?")
    try:
        if int(d) == 0:
            raise MyException('на ноль делить нельзя!')
        print(f"100 / {d} = {100 / int(d)}")
    except KeyboardInterrupt:
        break
    except ValueError:
        print("только целые числа!")
    except MyException as e:
        print(e._msg)
