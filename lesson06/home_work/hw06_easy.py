# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


# class Triangle:
#     a: int
#     b: int
#     c: int
#
#     def __init__(self, fist_side, second_side, third_side):
#         self.a = fist_side
#         self.b = second_side
#         self.c = third_side
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#     def _half_perimeter(self):
#         return self.perimeter() / 2
#
#     def triangle_square(self):
#         # return sqrt(3)
#         return sqrt(self._half_perimeter() * (self._half_perimeter() - self.a) * (self._half_perimeter() - self.b) * (self._half_perimeter() - self.c))
#
#     def height(self, value):
#         if value == self.a:
#             return self.triangle_square() / self.a
#         elif value == self.b:
#             return self.triangle_square() / self.b
#         elif value == self.c:
#             return self.triangle_square() / self.c
#         else:
#             print("ERROR")
#
#
# triangle = Triangle(3, 3, 3)
#
# print(triangle.perimeter())
# print(triangle.triangle_square())
# print(triangle.height(3))

class Point:
    x, y = 0, 0

    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def __str__(self):
        return str([self.x, self,y])


class Side:
    a, b = None, None

    def __init__(self, a: Point, b: Point):
        self.a, self.b = a, b

    def __str__(self):
        return f"Side: {self.a} -> {self.b}"

    @property
    def length(self):
        if self.a is not None and self.b is not None:
            vector = Point(self.b.x - self.a.x, self.b.y - self.a.y)
            value = math.sqrt((vector.x ** 2) + (vector.y ** 2))

            return round(value, 2) # simple number
        else:
            return 0

class Triangle:
    # Points: a, b, c
    def __init__(self, a: Point, b: Point, c: Point):
        self.a, self.b, self.c = a, b, c

    @property
    def ab(self):
        return Side(self.a, self.b).length

    @property
    def bc(self):
        return Side(self.b, self.c).length

    @property
    def ca(self):
        return Side(self.c, self.a).length

    def perimeter(self, full=True):
        p = round(self.ab + self.bc + self.ca, 5)

        return p if full else p / 2

    def area(self):
        p = self.perimeter(False)
        s = math.sqrt(p * (p - self.ab) * (p - self.bc) * (p - self.ca))

        return round(s, 5)

    def height(self):
        h = (2 * self.area()) / self.ab

        return round(h, 5)


triangle = Triangle(
    Point(1, 3),
    Point(5, 7),
    Point(6, 3)
)

print("#" * 10, 'Triangle', "#" * 10, )
print(triangle.ab)
print(triangle.bc)
print(triangle.ca)

print(triangle.perimeter())
print(triangle.area())
print(triangle.height())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# class equal_barrel:
#
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#     def _f(self, x, y):
#         return (x - y)**2
#
#     def checker(self):
#         ab = sqrt(sum(map(self._f, a, b)))
#         bc = sqrt(sum(map(self._f, b, c)))
#         cd = sqrt(sum(map(self._f, c, d)))
#         da = sqrt(sum(map(self._f, d, a)))
#         if ab == cd:
#             return print("Трапеция равнобокая")
#         elif bc == da:
#             return print("Трапеция равнобокая")
#         else:
#             return print("Трапеция не равнобокая")
#
#     def length(self, x, y):
#         return print(sqrt(sum(map(self._f, x, y))))
#
#
# a = [4, 4, 0]
# b = [0, 0, 0]
# c = [0, 3, 4]
# d = [1, 4, 4]
#
# equal_Barrel = equal_barrel(a, b, c, d)
# print(equal_barrel.length())
# # print(equal_barrel.checker())

class Trapeze:

    def __init__(self, a: Point, b: Point, c: Point, d: Point):
        self.a, self.b, self.c, self.d = a, b, c , d

    def __str__(self):
        return f"Trapeze: {self.a}, {self.b}, {self.c}, {self.d}"

    @property
    def ab(self):
        return Side(self.a, self.b).length

    @property # Основание верх
    def bc(self):
        return Side(self.b, self.c).length

    @property
    def cd(self):
        return Side(self.c, self.d).length

    @property # Основание низ
    def da(self):
        return Side(self.d, self.a).length

    def perimeter(self):
        return self.ab + self.bc + self.cd + self.da

    def height(self):
        numerator = ((self.da - self.bc) ** 2) + (self.ab ** 2) - (self.cd ** 2)
        denominator = 2 * (self.da - self.bc)

        h = math.sqrt(
            (self.ab ** 2) - ((numerator / denominator) ** 2)
        )

        return round(h, 2)

    def area(self):
        s = ((self.bc + self.da) * self.height()) / 2
        return round(s, 5)

    @property
    def is_equilateral(self):
        ac = Side(self.a, self.c)
        bd = Side(self.b, self.d)

        # Проверка диагоналей
        if ac.length == bd.length:
            return True
        else:
            return False

trapezoid = Trapeze(
    Point(1, 0),
    Point(3, 5),
    Point(6, 5),
    Point(8, 0)
)

print("#" * 10, 'Triangle', "#" * 10, )
print(trapezoid.ab)
print(trapezoid.bc)
print(trapezoid.cd)
print(trapezoid.da)

print(trapezoid.perimeter())
print(trapezoid.height())
print(trapezoid.area())
print(trapezoid.is_equilateral)

