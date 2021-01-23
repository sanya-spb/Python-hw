"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
 Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, color: str, name: str, speed: int = 0, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed: int):
        self.speed = speed
        print(f"поехали! скорость: {self.speed}км/ч")

    def stop(self):
        self.speed = 0
        print("остановились..")

    def turn(self, direction: str):
        print(f"повернули на {direction} на скорости {self.speed} км/ч")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
        return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
        return self.speed


class PoliceCar(Car):
    def __init__(self, color: str, name: str, speed: int = 0, is_police: bool = True):
        super().__init__(color, name, speed, is_police)


town_car = TownCar("blue", "vw")
sport_car = SportCar("red", "honda")
police_car = PoliceCar("green", "uaz")
work_car = WorkCar("gray", "Kamaz")

town_car.go(50)
town_car.turn("лево")
print(f"town_car speed: {town_car.show_speed()}")
town_car.go(120)
print(f"town_car speed: {town_car.show_speed()}")
town_car.stop()
print()
sport_car.go(120)
print(f"sport_car speed: {sport_car.show_speed()}")
print()
police_car.go(120)
print(f"police_car speed: {police_car.show_speed()}")
print()
work_car.go(30)
print(f"work_car speed: {work_car.show_speed()}")
work_car.go(60)
print(f"work_car speed: {work_car.show_speed()}")
