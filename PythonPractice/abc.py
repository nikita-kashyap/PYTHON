class vehicle:
    def__init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
        
    def display():
        return("name:",str(self.name)+"color:",str(self.color)+"pice:",str(self.price)
        
obj=vehicle
obj.display()

class car(vehicle):
    def change(self,number):
        self number=number
        print('car name is: ',str(self.name)+"car number:",str(self.number))

car_obj=car('audi','black',50000000)
car_obj.information()
car_obj.change(3)