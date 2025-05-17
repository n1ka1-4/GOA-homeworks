# 1) abstractclasses are function thats tells class to complite function by child class
# 2) in polymorphism we use abstractclasses but without ABC thats prevents from raising error
# 3) in aggregation we add one class to another

# 4
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        return "Meow!"
    
# 5
class shape:
    @abstractmethod
    def diameter(self):
        pass

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return self.radius * 2
    
# 6
class Dict:
    def __init__(self, name):
        self.name = name
        self.items = {}

    def add_book(self, book):
        self.items[book.category] = book.food

    def show_books(self):
        for category, food in self.items.items():
            print(f"{category}: {food}")


class Food:
    def __init__(self, food, category):
        self.food = food
        self.category = category

food1 = Food("brocoly", "vegetable")
food2 = Food("Burger", "Fast Food")
food3 = Food("Salad", "Healthy Food")

Cart = Dict("My Cart")

Cart.add_book(food1)
Cart.add_book(food2)
Cart.add_book(food3)

Cart.show_books()


    