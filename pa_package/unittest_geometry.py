import unittest
from point import Point
from line import Line
import math

class Test_geometry(unittest.TestCase):

    def test_distance_between_points(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)

        self.assertEqual(p1.distance_to(p2), 5.0)

    def test_distance_same_point(self):
        p1 = Point(2, 2)

        self.assertEqual(p1.distance_to(p1), 0.0)

    def test_line_length(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)

        line = Line(p1, p2)

        self.assertEqual(line.length(), 5.0)

    def test_horizontal_line_distance(self):
        p1 = Point(0, 0)
        p2 = Point(4, 0)

        line = Line(p1, p2)

        point = Point(2, 3)

        self.assertEqual(line.distance_to_point(point), 3.0)

    def test_vertical_line_distance(self):
        p1 = Point(0, 0)
        p2 = Point(0, 5)

        line = Line(p1, p2)

        point = Point(4, 2)

        self.assertEqual(line.distance_to_point(point), 4.0)


if __name__ == "__main__":
    unittest.main()
