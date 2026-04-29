class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return ((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2) ** 0.5

    def __str__(self):
        return f"Line({self.p1}, {self.p2})"


# test
p1 = Point(0, 0)
p2 = Point(3, 4)

line = Line(p1, p2)

print(line)
print("Length:", line.length())
