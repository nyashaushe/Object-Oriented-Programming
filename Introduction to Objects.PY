"""
class Dog():
    def __init__(self):
        pass

    def speak(self):
        pass

    #CLASS NAME IS DOG AND METhon is speak 


class Dog():
    def __init__(self):
        print("Created a dog")

    def speak(self):
        pass

me = Dog() 
"""


class Dog():
    def __init__(self, name):
        self.name = name  # self.name is now an attribute of the Dog class and has a specific value for each instance

    def speak(self):
        pass

tim = Dog("Tim") 



class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age 
     
    def speak(self):
        print("I am", self.name, "and I am", self.age, "years old")

    def change_age(self, age):
        self.age = age  # This changes the age attribute

    def add_weight(self, weight):
        self.weight = weight
        

tim = Dog("Tim", 5)
tim.change_age(7)
tim.speak() # This will print "I am Tim and I am 7 years old"
tim.add_weight(3)


print(tim.weight)