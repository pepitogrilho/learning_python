# -*- coding: utf-8 -*-
"""
"""

class BookShelf:
  def __init__(self, *books):
    self.books = books

  def __str__(self):
    return f"BookShelf with {len(self.books)} books."



class Book(BookShelf):
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Book {self.name}"
    
b1 = Book("Harry Potter")
b2 = Book("Title2")
b3 = Book("Title3")

shelf = BookShelf(b1, b2, b3)

print(shelf)