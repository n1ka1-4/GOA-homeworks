# 1 

# abstract methods is something from the abstract base class that makes functions give you errors if they are not implemented

# 2
 
# todays we learn about abstract base classes and how to use them how to create multiple inheritance and how to use super() to call the parent class constructor and multilevel inheritance 

# 3
class CSS:
    def __init__(self, selector, properties):
        self.selector = selector
        self.properties = properties

class Html:
    def __init__(self, tag, attributes):
        self.tag = tag
        self.attributes = attributes

class HtmlCss(Html, CSS):
    def __init__(self, tag, attributes, selector, properties):
        Html.__init__(self, tag, attributes)
        CSS.__init__(self, selector, properties)

    def apply(self):
        print(f"Applying {self.selector} to {self.tag} with properties {self.properties}")

# 4
class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name, hair_color):
        super().__init__(name)
        self.hair_color = hair_color
        

class Dog(Mammal):
    def __init__(self, name, hair_color, breed):
        super().__init__(name, hair_color)
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

# 5

# i already used super() in the previous code.
