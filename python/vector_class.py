class Vector:
    def __init__(self, values):
        self.values=values
    def __add__(self,other):
        q=[]
        if len(self.values) == len(other.values):
            for i in range(len(self.values)):
                q.append(self.values[i] + other.values[i])
        else:
            print("Error: dimension mismatch")
        
        return Vector(q)
    def __sub__(self,other):
        q=[]
        if len(self.values) == len(other.values):
            for i in range(len(self.values)):
                q.append(self.values[i] - other.values[i])
        else:
            print("Error: dimension mismatch")
        
        return Vector(q)
a = Vector([1,2,3])
b = Vector([4,3,8])
c = a - b
print(c.values)

x = Vector([10,10])
y = Vector([3,4])
print((x - y).values)