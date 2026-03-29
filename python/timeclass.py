'''
class Time24:
    def __init__(self, h, m):
       self.h=h
       self.m=m

    def __str__(self):
        if self.h==24:
            self.h=00
        if self.m==60:
            self.m=00
        
        if self.h < 10 and self.m < 10:
            return f"0{self.h}:0{self.m}"
        elif self.h < 10:
            return f"0{self.h}:{self.m}"
        elif self.h >= 10 and self.m < 10:
            return f"{self.h}:0{self.m}"
        elif self.h < 24 and self.m < 60:
            return f"{self.h}:{self.m}"
        
    def add_minutes(self, k):
        self.m=int(self.m) + int(k)
        if self.m >= 60:
            self.h=self.h + (self.m//60)
            self.m=self.m % 60
        elif self.m < 0:
            self.h=self.h - ((-self.m//60)+1)
            self.m = 60 + (self.m%60)
        if self.h < 0:
            self.h = 24 + (self.h % 24)
            
t = Time24(12, 30)
t.add_minutes(30)
print(str(t))
t.add_minutes(-90)
print(str(t))
'''

class Time24:
    def __init__(self, h, m):
       self.h = int(h)
       self.m = int(m)

    def __str__(self):
        if self.h==24:
            self.h=00
        if self.m==60:
            self.m=00
        
        if self.h < 10 and self.m < 10:
            return f"0{self.h}:0{self.m}"
        elif self.h < 10:
            return f"0{self.h}:{self.m}"
        elif self.h >= 10 and self.m < 10:
            return f"{self.h}:0{self.m}"
        elif self.h < 24 and self.m < 60:
            return f"{self.h}:{self.m}"
            
    def add_minutes(self, k):
        total = (self.h * 60 + self.m + int(k)) % (24 * 60)
        self.h = total // 60
        self.m = total % 60

t = Time24(12, 30)
t.add_minutes(30)
print(str(t))    
t.add_minutes(-90)
print(str(t))  
t = Time24(0, 0)
t.add_minutes(-1)
print(str(t))