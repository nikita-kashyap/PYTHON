class Vehicle():
    def __init__(self,name,color,price):
        self.name=name                  #   use self._varName for making any instance private
        self.color=color
        self.price=price
        
    def display(self):
        return (f"name:,{self.name}color:,str{self.color} price: {self.price}" )
        


class Car(Vehicle):
    def change(self,number):
        self.number=number
        print('car name is: ',str(self.name)+"car number:",str(self.number))

car_obj=Car('audi','black',50000000)
car_obj.information()
car_obj.change(3)

#collection framework
#dict and counter method try