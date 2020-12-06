# -*- coding: utf-8 -*-
"""
Class Methods receive the CLASS as argument
A common use of these are factory 
"""

class Book:
    TYPES = ("hardcover", "paperback")
    
    def __init__(self, name, book_type, weight):
      self.name = name
      self.book_type = book_type
      self.weight = weight
      
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight+100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight+50)

    def __repr__(self):
      return f"<Book {self.name}, {self.book_type}, weight {self.weight}g>"


print(Book.TYPES)

book = Book("HarryP", "hardcover", 1500)
print(book)

book2 = Book.hardcover("HarryP", 1500)
print(book2)

book3 = Book.paperback("Python 101", 600)
print(book3)