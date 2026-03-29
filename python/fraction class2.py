class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def gcd(self):
        a=1
        for i in range(min(abs(self.numer), abs(self.denom))):
            if self.numer % (i+1) == 0 and self.denom % (i+1) == 0:
                a = i+1
        return a
    def __str__(self):
        x = int(self.numer / int(Fraction.gcd(self)))
        y = int(self.denom / int(Fraction.gcd(self)))
        if (x>0 and y>0) or (x<0 and y<0):
            return f"{abs(x)}/{abs(y)}"
        else:
            return f"-{abs(x)}/{abs(y)}"

    def to_decimal(self):
        return self.numer / self.denom
        

f = Fraction(2, 4)
print(str(f), f.to_decimal())

f = Fraction(-2, 4)
print(str(f))

f = Fraction(2,-4)
print(str(f))

f = Fraction(0, 5)
print(str(f), f.to_decimal())

f = Fraction(3, -9)
print(str(f), f.to_decimal())