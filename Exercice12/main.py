import uuid

def refacto_search_book(list_books, book_title):
    for book in list_books:
        if book.title == book_title:
            return book

class Book:
    def __init__(self, title, author, year):
        self.id = uuid.uuid4()
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self, books=[], borrowed_books=[]):
        self.books = books
        self.borrowed_books = borrowed_books
    
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        book = refacto_search_book(self.books, book_title)
        self.books.remove(book)

    def borrow_book(self, book_title):
        book = refacto_search_book(self.books, book_title)
        self.borrowed_books.append(book)

    def return_book(self, book_title):
        book = refacto_search_book(self.books, book_title)
        self.borrowed_books.remove(book)

    def available_books(self):
        print("The avaible books of the Library are: ")
        all_books = self.books
        for borrowed in self.borrowed_books:
            if borrowed in all_books:
                all_books.remove(borrowed)
        
        for book in all_books:
            print(f"{book.title} - {book.author} ");\



    def borrowed_books_m(self):
        print("The borrowed books of the Library are:")
        for book in self.borrowed_books:
            print(f"{book.title} - {book.author} ")


book1 = Book(title="The mist", author="Shekspare", year=2000)
book2 = Book(title="The mist 2", author="Shekspare", year=2002)
book3 = Book(title="The Sun", author="Balzak", year=2003)
book4 = Book(title="I'm a false philosophe", author="Finkelcraut", year=1950)
book5 = Book(title="Book to delete", author='Glen Llaci', year=2025)
library = Library()

# adding books
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

# remove book
library.remove_book("Book to delete")

# Borrowing books
library.borrow_book("The Sun")
library.borrow_book("The mist")

# Borrowed books
library.borrowed_books_m()
print("_____")
library.available_books()
