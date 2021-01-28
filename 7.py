"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, a: int, b: int) -> None:
        # super().__init__()
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}+{self.b}i"

    def __add__(self, other):
        # z = (a1 + a2) + (b1 + b2)i
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        # z = (a1a2−b1b2) + (a1b2 + b1a2)i
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


z1 = Complex(3, 5)
z2 = Complex(2, 4)
print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"z1 + z2 = {z1 + z2}")
print(f"z1 * z2 = {z1 * z2}")
