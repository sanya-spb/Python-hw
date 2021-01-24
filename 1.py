"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix(object):
    def __init__(self, list_of_list):
        if isinstance(list_of_list, list):
            self._matrix = list_of_list
        else:
            raise TypeError("нужен список!")

    def __str__(self) -> str:
        if len(self._matrix) > 0:
            if isinstance(self._matrix[0], list):
                return "\n".join("\t".join(map(str, raw)) for raw in self._matrix)
            else:
                return "\t".join(map(str, self._matrix))
        else:
            return "[]"

    @property
    def as_list(self) -> list:
        return self._matrix

    @property
    def is_matrix(self) -> bool:
        if len(self._matrix) > 0:
            if isinstance(self._matrix[0], list):
                dim = len(self._matrix[0])
                for i in self._matrix:
                    if len(i) != dim:
                        return False
                return True
            else:
                return True
        else:
            return True

    @property
    def dim(self):
        if len(self._matrix) > 0:
            if isinstance(self._matrix[0], list):
                if self.is_matrix:
                    return [len(self._matrix[0]), len(self._matrix)]
                else:
                    return None
            else:
                return [len(self._matrix)]
        else:
            return [0]

    def __add__(self, other):
        if self.dim == other.dim:
            if self.dim == [0]:
                return self._matrix
            elif len(self.dim) == 1:
                return Matrix([sum(x) for x in zip(self._matrix, other.as_list)])
            else:
                i = 0
                result = []
                while i < self.dim[0]:
                    result.append([sum(x) for x in zip(self._matrix[i], other.as_list[i])])
                    i += 1
                return Matrix(result)
        else:
            raise TypeError("невозможно расчитать, разная размерность!")


# Exception: плохие входные данные, не список
# err1 = Matrix(1)
# print(err1)

err2 = Matrix([[1, 2, 3], [0, 0], [7, 8, 9]])
b23 = Matrix([[1, 2], [3, 4], [5, 6]])
print(f"err2\n{err2}\ndim(err2)={err2.dim}\n")
print(f"b23\n{b23}\ndim(b23)={b23.dim}\n")

a0 = Matrix([])
a3 = Matrix(
    [1, 2, 3]
)
b3 = Matrix(
    [10, 20, 30]
)
a33 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
b33 = Matrix([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(f"a0\n{a0}\ndim(a0)={a0.dim}\n")
print(f"a0 + a0\n{a0 + a0}\n")

print(f"a3\n{a3}\ndim(a3)={a3.dim}\n")
print(f"b3\n{b3}\ndim(b3)={b3.dim}\n")
print(f"a3 + b3\n{a3 + b3}\n")

print(f"a33\n{a33}\ndim(a33)={a33.dim}\n")
print(f"b33\n{b33}\ndim(b33)={b33.dim}\n")
print(f"a33 + b33\n{a33 + b33}\n")

# Exception: матрицы разных размерностей
# print(f"a33 + b22\n{a33 + b23}\n")
