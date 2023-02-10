class Shape():
    def __init__(self):
        pass
    def area(self, length, width):
        return 0

class Rectangle(Shape):
    def __init__(self, length = 0, width = 0):
        Shape.__init__(self)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

a = int(input())
b = int(input())
c = Rectangle(a, b)
print(a.area())

print(Rectangle().area())