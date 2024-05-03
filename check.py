from book_manager import BookManager  
from user_manager import UserManager 

book_manager = BookManager()  # Creating an instance of BookManager
user_manager = UserManager()  # Creating an instance of UserManager
checkouts = [] 


def checkout_book(user_id, isbn):
    """
    Checkout a book for a user.
    Args:
        user_id (int): The ID of the user.
        isbn (str): The ISBN of the book to checkout.
    Returns:
        str: A message indicating the success or failure of the operation.
    """
    user = next((u for u in user_manager.users if u.user_id == user_id), None)  # Find the user by user_id
    if not user:
        return "Error: No such user."

    book = next((b for b in book_manager.books if b.isbn == isbn), None)  # Find the book by ISBN
    if not book:
        return "Error: No such book."

    if any(c['isbn'] == isbn for c in checkouts):  # Check if the book is already checked out
        return "Error: Book already checked out."

    checkouts.append({"user_id": user_id, "isbn": isbn})  # Add the checkout record
    return f"Book {isbn} checked out to user {user_id}."


def checkin_book(isbn):
    """
    Check in a book.
    Args:
        isbn (str): The ISBN of the book to check in.

    Returns:
        str: A message indicating the success or failure of the operation.
    """
    global checkouts
    if any(c['isbn'] == isbn for c in checkouts):  # Check if the book is currently checked out
        checkouts = [c for c in checkouts if c['isbn'] != isbn]  # Remove the checkout record
        return f"Book {isbn} checked in successfully."
    return "Error: Book not currently checked out."


def list_checkouts():
    """
    List all book checkouts.

    Returns:
        str: A formatted string containing details of all book checkouts.
    """
    return "\n".join([f"User ID: {c['user_id']}, ISBN: {c['isbn']}" for c in checkouts])
