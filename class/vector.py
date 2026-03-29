class Vector:
    def __init__(self, v):
        self.v = v
    def magnitude(self):
        if len(v) == 2:
            return ((self.v[0])**2 + (self.v[1])**2)**0.5
        elif len(v) == 3:
            return ((self.v[0])**2 + (self.v[1])**2 + (self.v[2])**2)**0.5

def cross_product(v1,v2):
    if len(v1.v) == 2 or len(v2.v) == 2:
        return "Error: cross product is defined for 3D vectors"
    elif len(v1.v) == 3 or len(v2.v) == 3:
        x= v1.v[1]*v2.v[2] - v2.v[1]*v1.v[2]
        y= -v1.v[0]*v2.v[2] + v2.v[0]*v1.v[2]
        z= -v1.v[1]*v2.v[0] + v2.v[1]*v1.v[0]
        v=[x,y,z]
        return Vector(v)

a = Vector([1,2,3])
b = Vector([4,5,6])
print(cross_product(a,b).v)

a = Vector([1,2,3])
b = Vector([1,4,3])
print(cross_product(a,b).v)

