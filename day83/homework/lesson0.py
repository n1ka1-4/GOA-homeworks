# 1
class Motorcycle:
    COUNT = 0
    def __init__(self, make, model, year, clr):
        self.make = make
        self.model = model
        self.year = year

# 2
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

# 3

# inheritance is working by creating a new class that is a child of the parent class and we do this by using the class name and putting the parent class in parentheses and using the super() function to call the parent class constructor

# 4

# we use inheritance for faster defining veriables and more efficient code

# 5

# multyple inheritance is when a class is inherited from more than one parent class by using the class name and putting the parent classes in parentheses plus saperated by commas and using the class name function to call the parent class constructor