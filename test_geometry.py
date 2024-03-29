import unittest

from geometry.geometry import Circle, Triangle


class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(Circle.circle_area(35), 3848.4510006474966)

    def test_triangle_area(self):
        self.assertAlmostEqual(Triangle.triangle_area(5, 3, 4), 6.0)
        self.assertAlmostEqual(
            Triangle.triangle_area(8, 1, 1),
            'Такого треугольника не существует!',
        )

    def test_is_right_triangle(self):
        self.assertTrue(Triangle.is_right_triangle(3, 4, 5))
        self.assertFalse(Triangle.is_right_triangle(8, 2, 4))


if __name__ == '__main__':
    unittest.main()
