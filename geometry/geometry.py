import math


class Circle:
    @staticmethod
    def circle_area(radius: int | float) -> float:
        '''Вычисляет площадь круга.'''

        return math.pi * (radius**2)


class Triangle:
    @staticmethod
    def triangle_area(
        first_side: int | float,
        second_side: int | float,
        third_side: int | float,
    ) -> float:
        '''Вычисляет площадь треугольника по трем сторонам.'''

        p = (first_side + second_side + third_side) / 2
        try:
            return math.sqrt(
                p * (p - first_side) * (p - second_side) * (p - third_side)
            )
        except ValueError:
            return 'Такого треугольника не существует!'

    @staticmethod
    def is_right_triangle(
        first_side: int | float,
        second_side: int | float,
        third_side: int | float,
    ) -> bool:
        '''Проверка на то, является ли треугольник прямоугольным.'''

        sides = [first_side, second_side, third_side]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
