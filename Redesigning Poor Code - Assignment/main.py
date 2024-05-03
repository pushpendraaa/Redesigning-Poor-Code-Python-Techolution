from book_manager import BookManager
from user_manager import UserManager
from check import checkout_book, checkin_book, list_checkouts

def main_menu():
    print("Welcome to the Library Management System!!")
    while True:
        print("\n1. Manage Books")
        print("2. Manage Users")
        print("3. Check Out Book")
        print("4. Check In Book")
        print("5. List All Checkouts")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            manage_books()
        elif choice == '2':
            manage_users()
        elif choice == '3':
            perform_checkout()
        elif choice == '4':
            perform_checkin()
        elif choice == '5':
            print(list_checkouts())
        elif choice == '6':
            print("System Exited!")
            break
        else:
            print("Invalid option, please 1try again.")

def manage_books():
    bm = BookManager()
    valid_attributes = ['title','author', 'isbn'] 
    while True:
        print("\n1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Books")
        print("5. Back")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            print(bm.add_book(title, author, isbn))
        elif choice == '2':
            isbn = input("Enter ISBN to remove: ")
            print(bm.remove_book(isbn))
        elif choice == '3':
            print("Books List:")
            print(bm.list_books())
        elif choice == '4':
            search_attribute = input("Search by (title, author, isbn): ").lower()
            if search_attribute in valid_attributes:
                search_value = input(f"Enter {search_attribute}: ")
                search_results = bm.search_books(**{search_attribute: search_value})
                if isinstance(search_results, list):
                    for book in search_results:
                        print(book)
                else:
                    print(search_results)
            else:
                print("Invalid search. Please choose from title, author, or isbn.")
        elif choice == '5':
            break
        else:
            print("Invalid option!!!, please try again.")



def manage_users():
    um = UserManager()
    while True:
        print("\n1. Add user\n2. Remove user\n3. List users\n4. Back")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            print(um.add_user(name, user_id))
        elif choice == '2':
            user_id = input("Enter user ID to remove: ")
            print(um.remove_user(user_id))
        elif choice == '3':
            print("Users List:")
            print(um.list_users())
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")

def perform_checkout():
    user_id = input("Enter user ID: ")
    isbn = input("Enter book ISBN: ")
    result = checkout_book(user_id, isbn)
    print(result)

def perform_checkin():
    isbn = input("Enter book ISBN to check in: ")
    result = checkin_book(isbn)
    print(result)

if __name__ == "__main__":
    main_menu()
