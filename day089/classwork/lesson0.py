# 1
# deference between aggregation and composition is that in aggregation one class is not dependent on the other class, while in composition one class is dependent on the other class.
class Bed:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def __str__(self):
        return f"Bed(length={self.length}, width={self.width}, height={self.height})"
    
class Home:
    def __init__(self, address, size):
        self.address = address
        self.size = size
        self.bed = Bed(100, 200, 50)

# 2
# for instance method we use "self" thats means "object" and for class method we use "cls" that means "class" + @classmethod decorator and for static method we not use self nor cls. it is independent of class and object. it is just function in class + @staticmethod decorator.

# 3
# multiple inheritance is when a class inherits from multiple classes. for example, class A inherits from class B and class C at the same time.
# multi-level inheritance is when a class inherits from another class which is inherits from another class. for example, class A inherits from class B and class B inherits from class C.

#
class User:
    def __init__(self, name, email, password):
        # "_" is used to say that this variable is protected and should not be accessed directly from outside the class. (it have to be used inside the class)
        self._name = name

        # "__" is used to say that this variable is private and should not be accessed directly from outside the class. (it must not used outside the class)
        self.__email = email
        self.__password = password

    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def get_name(self):
        return self._name