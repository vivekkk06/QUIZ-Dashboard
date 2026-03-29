class Vector:
    def __init__(self,values):
        self.values=values
        
    def magnitude(self):
        return (self.values[0]**2 + self.values[1]**2)**0.5
        
def cross_product(self,other):
    x=self.values[1]*other.values[2] - self.values[2]*other.values[1]
    y=self.values[2]*other.values[0] - self.values[0]*other.values[2]
    z=self.values[0]*other.values[1] - self.values[1]*other.values[0]
    return Vector([x,y,z])
a = Vector([1,2,3])
b = Vector([4,5,6])
print(cross_product(a,b).values)