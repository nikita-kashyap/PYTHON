class Area:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.radius**2*3.14

class Circumfrence(Area):

    def circum(self):
        return self.radius*2*3.14

obj=Circumfrence(5)
print(obj.area())
print(obj.circum())