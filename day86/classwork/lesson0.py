# 1
from abc import ABC, abstractmethod

# requares sound function to be implemented in all subclasses
# if not implemented, it will raise an error
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"
    
# 2

# requires area function to be implemented in all subclasses
# but does not raise an error
class shape:

    @abstractmethod
    def area(self):
        pass

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
# 4
class Dict:
    def __init__(self, name):
        self.name = name
        self.items = {}

    def add_book(self, book):
        self.items[book.author] = book.title

    def show_books(self):
        for author, title in self.items.items():
            print(f"{author}: {title}")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

library = Dict("My Library")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()

