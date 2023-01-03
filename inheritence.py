from abc import abstractmethod, ABCMeta
import math

class Shape(object):
 __metaclass__ = ABCMeta # If this is not used, child class inheriting and not implementing abstractmethods will not produce error.
 @abstractmethod
 def area(self):
            pass
 @abstractmethod
 def perimeter(self):
            pass

class Rectangle(Shape): #Rectangle inheriting Shape class.
 def __init__(self, length, height):
  self.length = length
  self.height = height
  super(Rectangle, self).__init__()
 def area(self):
  return self.length * self.height
 def perimeter(self):
  return self.length * 2 + self.height * 2

class Square(Rectangle):
 def __init__(self, sid_length):
  self.side = sid_length
  super(Square, self).__init__(self.side, self.side)

class Triangle(Rectangle): # for simplicity we take right angled triangle, area = bh/2 and perimeter = b + h + sqroot(b*b + h*h)
    def __init__(self, base, height):
        self.base = base
        self.height = height
        super(Triangle, self).__init__(self.base, self.height) # if we dont use this, variables in parent class will not be initialised.
    def area(self):
        y = super(Triangle, self).area()
        return float(y) / 2
    def perimeter(self):
        return self.base + self.height + math.sqrt(self.base * self.base + self.height * self.height)

class Circle(Rectangle):
    def __init__(self, radius):
        self.radius = radius
        super(Circle, self).__init__(self.radius, self.radius)
    def area(self):
        y = super(Circle, self).area()
        return 3.14 * y
    def perimeter(self):
        return 2 * 3.14 * self.radius

r = Rectangle(10, 10)
print(r.area())
print(r.perimeter())
s = Square(10)
print(s.area())
print(s.perimeter())
t = Triangle(1, 1)
print(t.area())
print(t.perimeter())
c = Circle(10)
print(c.area())
print(c.perimeter())