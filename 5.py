"""
6. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки. title: {self.title}")


class Pen(Stationery):
    def draw(self):
        super().draw()
        print("уникальная ручка")


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print("уникальный карандаш")


class Handle(Stationery):
    def draw(self):
        super().draw()
        print("уникальный маркер")


pen = Pen("типа Ручка")
pencil = Pencil("типа Карандаш")
handle = Handle("типа Маркер")

pen.draw()
pencil.draw()
handle.draw()
