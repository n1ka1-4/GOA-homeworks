# 1. Initialization - __init__ method defines the constructor of the class. It is called when an object of the class is created. It initializes the instance variables of the class.
# 2. Class variables - class veriables are defined inside the class not inside the __init__ method and are shared by all instances of the class. They are accessed using the class name or the instance of the class.
# 3. Instance methods - instance methods are defined inside the class and are called on instances of the class. They are accessed using the instance of the class. They take "self" as the first parameter which refers to the instance of the class.
# 4. Inheritance - inheritance is when a class inherits from another class. The class that inherits is called the child class and the class that is inherited from is called the parent class. The child class can access the methods and variables of the parent class.
# 5. Multiple inheritance - multiple inheritance is when a class inherits from multiple classes.
# 6. Multilevel inheritance - multilevel inheritance is when a class inherits from another class which is inherited from another class. For example, class A inherits from class B and class B inherits from class C.
# 7. super() - super() is used to call the constructor of the parent class. It is used in the child class to access the methods and variables of the parent class.
# 8. Abstract classes - abstract classes are classes that makes class incomplete and needs to be completed by the child class. They are defined using the abc module and the ABC class. by using ABC class it demands the child class to implement the abstract methods of the parent class. but with out ABC it does not demand the child class to implement the abstract methods of the parent class.
# 9. Polymorphism - polymorphism is the ability of an object to take on many forms. It is the ability to call the same method on different objects and get different results. like len() method can be used on different objects like list, string, tuple, etc. and it will return the length of the object.
# 10. Duck typing - duck typing is a form of polymorphism where the type of the object is not important. It is the ability to call the same method on different objects and get different results. but in duck typing we don't use class inheritance. for example, if an object has a method called "quack" then it is considered to be a duck. It does not matter if the object is actually a duck or not. It just needs to have the method "quack".
# 11. Aggregation - aggregation is when one class is not dependent on the other class, but they are related. For example, a class "Home" can have a class "Bed" as an attribute. The class "Home" is not dependent on the class "Bed". The class "Bed" can exist without the class "Home".
# 12. Composition - composition is when one class is dependent on the other class. For example, a class "Home" can have a class "Bed" as an attribute. The class "Bed" is depend on the class "Home". The class "Bed" cannot exist without the class "Home".
# 13. Static methods - static methods are defined inside the class and are called on the class itself. They are accessed using the class name. They do not take "self" or "cls" as the first parameter. They are just like normal functions but they are defined inside the class and we use @staticmethod decorator to define static methods.
# 14. Class methods - class methods are defined inside the class and are called on the class itself. They are accessed using the class name. They take "cls" as the first parameter which refers to the class itself. They are used to access the class variables and methods and we use @classmethod decorator to define class methods.
# 15. Data hiding - data hiding is the process of hiding the data members of a class from the outside world. It is done using "_" and "__" before the variable name. "_" is used to say that this variable is protected and should not be accessed directly from outside the class (it is for other programmers). "__" is used to say that this variable is private and should not be accessed directly from outside the class.

# 1
combat = lambda health, damage: max(0, health - damage)
    
# 2
def how_many_light_sabers_do_you_own(name=""):
    return 18 if name is "Zach" else 0

# 3
def stringy(size):
    return (size // 2) * "10" if size % 2 == 0 else (size // 2) * "10" + "1"

# 4
def mouth_size(animal): 
    return "small" if animal.lower() == "alligator" else "wide"

# 5
def distinct(seq):
    return sorted(set(seq), key=lambda x: seq.index(x))

# 6
def nth_even(n):
    return n * 2 - 2

# 7
def warn_the_sheep(queue):
    s = queue[::-1].index("wolf")
    return "Pls go away and stop eating my sheep" if queue[-1] == "wolf" else f"Oi! Sheep number {s}! You are about to be eaten by a wolf!"

# 8
def flip(d, a):
     return sorted(a) if d == "R" else sorted(a)[::-1]

# 9
def well(x):
    return "Fail!" if all(i == "bad" for i in x) else "Publish!" if x.count("good") < 3 else "I smell a series!" 

# 10
class Ball:
    def __init__(self,s=None):
        self.s = s
        self.ball_type = "regular" if s == None else "super"