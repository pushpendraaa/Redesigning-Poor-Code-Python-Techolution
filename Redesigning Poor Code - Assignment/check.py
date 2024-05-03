from book_manager import BookManager
from user_manager import UserManager
book_manager = BookManager()
user_manager = UserManager()
checkouts = []
def checkout_book(user_id, isbn):
    user = next((u for u in user_manager.users if u.user_id == user_id), None)
    if not user:
        return "Error: No such user."
    book = next((b for b in book_manager.books if b.isbn == isbn), None)
    if not book:
        return "Error: No such book."
    if any(c['isbn'] == isbn for c in checkouts):
        return "Error: Book already checked out."
    checkouts.append({"user_id": user_id, "isbn": isbn})
    return f"Book {isbn} checked out to user {user_id}."

def checkin_book(isbn):
    global checkouts
    if any(c['isbn'] == isbn for c in checkouts):
        checkouts = [c for c in checkouts if c['isbn'] != isbn]
        return f"Book {isbn} checked in successfully."
    return "Error: Book not currently checked out."

def list_checkouts():
    return "\n".join([f"User ID: {c['user_id']}, ISBN: {c['isbn']}" for c in checkouts])
