class Circle:
    PI=3.14
    def __init__(self,radius):
        self.radius=radius

    def calArea(self):
        return 2*self.PI.radius**2

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calArea(self):
        return self.length*self.width
obj=Rectangle
# obj.calArea(4)
obj.calArea(4,5)