class rectangle:
    def __init__(self, point, width, height):
        self.point=point
        self.width = width
        self.height = height
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return 2*(self.width + self.height)
    def contains(self, other):
        if (other.x >= self.point.x and other.x <= (self.point.x + self.width)) and (other.y <= self.point.y and other.y >= (self.point.y - self.height)):
            return True
        else:
            return False

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

r = rectangle(point(0, 10), 10, 5)
print(r.area(), r.perimeter())

r = rectangle(point(0, 0), 4, 4)
print(r.contains(point(2,-2)))

r = rectangle(point(-5, 5), 10, 10)
print(r.contains(point(-5, 5)))

r = rectangle(point(0, 0), 4, 4)
print(r.contains(point(8,-2)))