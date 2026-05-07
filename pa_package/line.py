import math
from point import Point

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return self.p1.distance_to(self.p2)

    def distance_to_point(self, point):
        """
        Perpendicular distance from a point to the line
        using the line equation formula.
        """

        x0, y0 = point.x, point.y
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y

        numerator = abs(
            (y2 - y1) * x0 -
            (x2 - x1) * y0 +
            x2 * y1 -
            y2 * x1
        )

        denominator = math.sqrt(
            (y2 - y1) ** 2 +
            (x2 - x1) ** 2
        )

        return numerator / denominator

    def __str__(self):
        return f"Line({self.p1}, {self.p2})"