"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Store:

    def __init__(self, name: str):
        self.name = name


class OfficeEquipment:

    def __init__(self, model_name: str, type_of_equip: str):
        self.type_of_equip = type_of_equip
        self.model_name = model_name


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
