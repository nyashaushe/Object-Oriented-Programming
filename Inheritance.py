"""class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def speak(self):
        print("I am", self.name, "and I am", self.age, "years old")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = "dog"

    # Since we inherit from the animal class we can use the method speak on Dog objects
    #class Dog got info from Animal Class- inherited all animal methods


tim = Dog("Tim", 5)
tim.speak() # This will print "I am Tim and I am 5 years old" 
"""



class Veichle:
    def __init__(self, price, color):
        self.color = color
        self.price = price
        self.gas = 0

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Truck(Veichle):
    def __init__(self, price, color, tires):
        super().__init__(price, color)
        self.tires = tires

    def beep(self):
        print("Honk honk")


class Car(Veichle):
    def __init__(self, price, color, speed):
        super().__init__(price, color)
        self.speed = speed

    def beep(self):
        print("Beep Beep")


my_fleet=Veichle(500, "green")
fleet_type =Truck(200,"red", "17.5r")
my_fleet.fillUpTank()
fleet_type.beep()


print("Total fleet gas amount",my_fleet.gas,"litres")
