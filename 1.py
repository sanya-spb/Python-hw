"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_str: str):
        if Date.pass_date(date_str):
            self._date_str = date_str
        else:
            print("неверный формат данных")

    def __str__(self) -> str:
        tmp = Date.extract_date(self._date_str)
        return f"{tmp[0]:02d}/{tmp[1]:02d}/{tmp[2]:04d}".format(tmp)

    @classmethod
    def extract_date(cls, date_str: str):
        d = date_str.split('-')
        for i in range(len(d)):
            try:
                d[i] = int(d[i])
            except ValueError:
                raise TypeError("Формат: dd-mm-yyyy, должны быть все числа, c разделителем '-'!")
        try:
            return d[0], d[1], d[2]
        except IndexError:
            raise TypeError("Формат: dd-mm-yyyy!")

    @staticmethod
    def pass_date(date_str: str) -> bool:
        dd, mm, yyyy = Date.extract_date(date_str)

        if dd > 0 and dd <= 31 and mm > 0 and mm <= 12 and yyyy > 1900 and yyyy <= 3000:
            if yyyy % 4 != 0 or (yyyy % 100 == 0 and yyyy % 400 != 0):
                if mm == 2 and dd > 28:
                    print("Формат: dd-mm-yyyy, неверный формат даты (невисокосного года)!")
                    return False
            elif mm == 2 and dd > 29:
                print("Формат: dd-mm-yyyy, неверный формат даты (високосного года)!")
                return False
        else:
            print("Формат: dd-mm-yyyy, неверный формат даты (выход за пределы)!")
            return False
        return True


print(f"Date('12-1-2021'):\t{Date('12-1-2021')}")
print(f"Date.extract_date('12-1-2021'):\t{Date.extract_date('12-1-2021')}")
for d in [
    '12.1.2021',
    '32-2-2021',
    '30-2-2021',
    '29-2-2021',
    '29-2-2020',
]:
    try:
        print(d)
        print(Date.pass_date(d))
    except TypeError as e:
        print(str(e))
