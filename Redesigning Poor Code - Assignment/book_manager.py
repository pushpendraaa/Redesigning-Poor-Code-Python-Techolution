import json
from book import Book

class BookManager:
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r') as f:
                books_data = json.load(f)
                return [Book(**book) for book in books_data]
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.filename, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f)

    def add_book(self, title, author, isbn):
        if any(book.isbn == isbn for book in self.books):
            return "Book with this ISBN already exists."
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        return "Book added"

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books()
                return "Book removed"
        return "Book not found."

    def list_books(self):
        return "\n".join(str(book) for book in self.books if book)

    def search_books(self, **kwargs):
        found_books = []
        for book in self.books:
            if all(getattr(book, key, None) == value for key, value in kwargs.items()):
                found_books.append(book)
        return found_books if found_books else "No books found"

