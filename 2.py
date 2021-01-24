"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, height):
        self._V = size
        self._H = height

    @property
    def coat_consumption(self):
        if self._V:
            return self._V / 6.5 + 0.5
        else:
            return 0

    @property
    def suit_consumption(self):
        if self._H:
            return self._H * 2 + 0.3
        else:
            return 0

    @property
    def sum_cloth_consumption(self):
        return round(self.coat_consumption + self.suit_consumption, 2)

    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        super(Coat, self).__init__(size, None)
        self._V = size

    @property
    def cloth_consumption(self):
        return round(self.coat_consumption, 2)


class Suit(Clothes):
    def __init__(self, height):
        super(Suit, self).__init__(None, height)
        self._H = height

    @property
    def cloth_consumption(self):
        return round(self.suit_consumption, 2)


coat = Coat(154)
print(coat.cloth_consumption)

suit = Suit(75)
print(suit.cloth_consumption)

print(coat.sum_cloth_consumption)
print(suit.sum_cloth_consumption)
