class Book:
    def __init__(self, title, author, isbn):
        """
        Constructor method to initialize a Book object.
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN (International Standard Book Number) of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """
        String representation of the Book object.
        Returns:
            str: A string representation of the book in the format "Title by Author, ISBN: xxx".
        """
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"
