import unittest
import circle
import rectangle
import square
import triangle
import math

class CircleTestCase(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(circle.area(0), 0.0)
        self.assertEqual(circle.perimeter(0), 0.0)

    def test_one_radius(self):
        self.assertEqual(circle.area(1), math.pi)
        self.assertEqual(circle.perimeter(1), 2 * math.pi)

    def test_float_radius(self):
        r = 2.5
        self.assertEqual(circle.area(r), math.pi * r * r)
        self.assertEqual(circle.perimeter(r), 2 * math.pi * r)

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = rectangle.area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = rectangle.area(10, 10)
       self.assertEqual(res, 100)

    def test_different_mul(self):
       res = rectangle.area(10, 20)
       self.assertEqual(res, 200)

    def test_float_mul(self):
       res = rectangle.area(5.5, 5.5)
       self.assertEqual(res, 30.25)

class SquareTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(square.area(0), 0.0)
        self.assertEqual(square.perimeter(0), 0.0)

    def test_positive_side(self):
        self.assertEqual(square.area(5), 25.0)
        self.assertEqual(square.perimeter(5), 20.0)

    def test_float_side(self):
        self.assertEqual(square.area(2.5), 6.25)
        self.assertEqual(square.perimeter(2.5), 10.0)

class TriangleTestCase(unittest.TestCase):
    def test_zero_height(self):
        self.assertEqual(triangle.area(10, 0), 0.0)

    def test_zero_base(self):
        self.assertEqual(triangle.area(0, 10), 0.0)

    def test_sides_3_4_5(self):
        self.assertEqual(triangle.area(3, 4), 6.0)
        self.assertEqual(triangle.perimeter(3, 4, 5), 12.0)

    def test_float_sides(self):
        self.assertEqual(triangle.perimeter(2.5, 3.5, 4.0), 10.0)
