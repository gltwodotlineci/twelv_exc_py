import uuid

def refacto_search_book(list_books, book_title):
    for book in list_books:
        if book.title == book_title:
            return book

def refacto_error(books, book_title):
    if book_title not in books:
        raise ValueError("Wrong title, please try again!")


class Book:
    def __init__(self, title, author, year):
        self.id = uuid.uuid4()
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self, books=None, borrowed_books=None):
        self.books = books or {}
        self.borrowed_books = borrowed_books or {}
    
    def add_book(self, book):
        self.books[book.title] = book

    # Remove book from the library
    def remove_book(self, book_title):
        refacto_error(self.books, book_title)
        self.books.pop(book_title)

    # Borrow book from library
    def borrow_book(self, book_title):
        refacto_error(self.books, book_title)
        self.borrowed_books[book_title] = self.books.get(book_title)

    # Returning book on the library
    def return_book(self, book_title):
        refacto_error(self.books, book_title)
        if self.borrowed_books.get(book_title) is None:
            raise ValueError("The book is not borrowed")

        self.borrowed_books.pop(book_title)

    # Return the list of Available books
    def available_books(self):
        print("The avaible books of the Library are: ")
        for k, book in self.books.items():
            if book not in self.borrowed_books:
                print(f"{k} - {book.author} ")


    def borrowed_books_m(self):
        print("The borrowed books of the Library are:")
        for k, book in self.borrowed_books.items():
            print(f"{k} - {book.author} ")


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
library.borrow_book("The mist 2")

# Returning book
library.return_book('The mist 2')
print("   ")
print(library.__dict__)

# Borrowed books
library.borrowed_books_m()
print("_____")
library.available_books()
