class Dog:
    def __init__(self,breed):
        self.breed=breed

class Circle:
  
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.radius**2*3.14

    def circumfrence(self):
        return self.radius*2*3.14

name=Dog(breed="pitbull")
print(name.breed)

obj=Circle(radius=8)
print(obj.area())
print(obj.circumfrence())

    