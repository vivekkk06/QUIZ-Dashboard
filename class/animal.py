class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "...."
class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Meow"
class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Woof"

pets = [Animal('Xavier'), Dog('A'), Cat('B'), Dog('C')]
print([p.speak() for p in pets])

x = Dog('Bruno')
a = x # Animal reference
print(a.speak())

print(isinstance(Dog('D'), Animal), isinstance(Cat('E'), Animal))