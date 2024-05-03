import json
from book import Book  # Assuming Book class is defined in book.py

class BookManager:
    def __init__(self, filename='books.json'):
        """
        Constructor method to initialize a BookManager object.
        Args:
            filename (str): The name of the JSON file to load/save book data.
        """
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        """
        Load books data from a JSON file.
        Returns:
            list: A list of Book objects loaded from the JSON file.
        """
        try:
            with open(self.filename, 'r') as f:
                books_data = json.load(f)
                return [Book(**book) for book in books_data]
        except FileNotFoundError:
            return []

    def save_books(self):
        # Save books data to a JSON file.
        with open(self.filename, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f)

    def add_book(self, title, author, isbn):
        """
        Add a new book to the collection.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        Returns:
            str: A message indicating the success or failure of the operation.
        """
        if any(book.isbn == isbn for book in self.books):
            return "Book with this ISBN already exists."
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        return "Book added"

    def remove_book(self, isbn):
        """
        Remove a book from the collection by ISBN.
        Args:
            isbn (str): The ISBN of the book to remove.

        Returns:
            str: A message indicating the success or failure of the operation.
        """
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books()
                return "Book removed"
        return "Book not found."

    def list_books(self):
        """
        Generate a string containing details of all books in the collection.
        Returns:
            str: A formatted string containing details of all books.
        """
        return "\n".join(str(book) for book in self.books if book)

    def search_books(self, **kwargs):
        """
        Search for books in the collection based on specified criteria.
        Args:
            kwargs: Keyword arguments representing search criteria (e.g., title, author, isbn).
        Returns:
            list or str: A list of matching Book objects or a message indicating no books found.
        """
        found_books = []
        for book in self.books:
            if all(getattr(book, key, None) == value for key, value in kwargs.items()):
                found_books.append(book)
        return found_books if found_books else "No books found"
