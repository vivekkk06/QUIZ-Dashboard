class Point:
    num_points = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
        Point.num_points += 1
    def __del__(self):
        Point.num_points -= 1
        print(f"point({self.x},{self.y}) deleted")

p = Point(1, 2)
print(Point.num_points)
del p
print(Point.num_points)
