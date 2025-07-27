class Shape:
    def __init__(self):
        self.name = "Shape"

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

s = Rectangle(10, 5)
print("Rectangle Area:", s.area())
