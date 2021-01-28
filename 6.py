"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self) -> str:
        return self.msg


class Store:
    store_detail = {}

    def __init__(self, name: str):
        self.name = name

    def to_store(self, model_name, count: int):
        if not isinstance(count, int):
            raise MyException("надо указать количество цифрой!")
        if model_name in self.store_detail:
            self.store_detail[model_name]["on_store"] += count
        else:
            self.store_detail[model_name] = {"on_store": count}
            self.store_detail[model_name]["on_division"] = {}
        print(f"на склад поступило {model_name}: {count}шт.")

    def to_company(self, division: str, model_name, count: int):
        if model_name in self.store_detail:
            if self.store_detail[model_name]["on_store"] >= count:
                self.store_detail[model_name]["on_store"] -= count
                if division in self.store_detail[model_name]["on_division"]:
                    self.store_detail[model_name]["on_division"][division] += count
                else:
                    self.store_detail[model_name]["on_division"][division] = count
            else:
                print("нет небходимого количества а складе")
        else:
            print("данная модель отсутствует на складе")
        print(f"со склада ушло {model_name}: {count}шт в отдел: {division}.")


class OfficeEquipment:

    def __init__(self, model_name: str, type_of_equip: str):
        self.type_of_equip = type_of_equip
        self.model_name = model_name

    def __repr__(self) -> str:
        return self.model_name


class Printer(OfficeEquipment):

    def __init__(self, model_name: str, color: bool):
        super().__init__(model_name, "Принтер")
        self.color = color


class Scanner(OfficeEquipment):

    def __init__(self, model_name: str, dpi: int):
        super().__init__(model_name, "Сканер")
        self.dpi = dpi


class Xerox(OfficeEquipment):

    def __init__(self, model_name: str, speed: int):
        super().__init__(model_name, "Ксерокс")
        self.speed = speed


store = Store("Склад")
printer1 = Printer("printer1", True)
scanner1 = Scanner("scanner1", 1200)
xerox1 = Xerox("xerox1", 100)

# поступление на склад
for office_equipment, count in (dict(zip([printer1, scanner1, xerox1], [10, "десять", 4])).items()):
    try:
        store.to_store(office_equipment, count)
    except MyException as e:
        print(e.msg)
print(store.store_detail)

# со склада по отделам
for division, count in (dict(zip(["IT", "Бухи", "Секретарь"], [5, 4, 1])).items()):
    store.to_company(division, printer1, count)
for division, count in (dict(zip(["IT", "Бухи", "Секретарь"], [0, 1, 1])).items()):
    store.to_company(division, xerox1, count)
print(store.store_detail)
