# 1
class Car:
    def __init__(self, make, model, year, clr):
        self.make = make
        self.model = model
        self.year = year
        self.clr = clr

    def sound(self):
        return "Vroom!"
    
    def move(self):
        return "The car is moving!"
    

car1 = Car("Toyota", "Corolla", 2020, "Red")
car2 = Car("Honda", "Civic", 2021, "Blue")
car3 = Car("Ford", "Mustang", 2022, "Black")

print(car1.sound())
print(car1.move())
print(car2.make)
print(car2.model)
print(car3.year)
print(car3.clr)

# 2
class People:

    PEOPLE_COUNT = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        People.PEOPLE_COUNT += 1

    def moving(self):
        return "The person is moving!"
    
    def speaking(self):
        return "The person is speaking!"
    

person1 = People("John", 30, 180)
person2 = People("Jane", 25, 170)
person3 = People("Doe", 28, 175)
person4 = People("Smith", 35, 185)
person5 = People("Brown", 22, 160)

print(person1.moving())
print(person1.speaking())
print(person2.name)
print(person2.age)
print(person2.height)
print(People.PEOPLE_COUNT)

# 3

# dunder methods is a special method that starts and ends with double underscores.

# 4

# instance variable is a variable that is bound to the instance of the class.

# 5

# class variable is a variable that is bound to the class and not the instance of the class.

# 6

# blueprint is a template for creating objects. its called a blueprint because it defines the structure and behavior of the objects that will be created from it.
