import book
import check
import storage
import logging

def log(operation, user_id=None, isbn=None, title=None, author=None):
    if user_id:
        logging.info(f"User ID: {user_id}")
    if isbn:
        logging.info(f"ISBN: {isbn}")
    if title:
        logging.info(f"Title: {title}")
    if author:
        logging.info(f"Author: {author}")
    logging.info(f"Operation: {operation}")

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Checkout Book")
    print("5. Return Book")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid choice, please try again.")
        return None
    return choice

def main():
    logging.basicConfig(filename='library.log', level=logging.INFO)

    library = storage.Library()
    user_manager = storage.UserManager()
    checkout_manager = storage.CheckoutManager()

    while True:
        try:
            choice = main_menu()
            if choice == 1:
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                log("Add Book", title=title, author=author, isbn=isbn)
                library.add_book(book.Book(title, author, isbn))
                print("Book added.")
            elif choice == 2:
                log("List Books")
                library.list_books()
            elif choice == 3:
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                log("Add User", user_id=user_id)
                user_manager.add_user(name, user_id)
                print("User added.")
            elif choice == 4:
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                log("Checkout Book", user_id=user_id, isbn=isbn)
                checkout_manager.checkout_book(library, user_manager, user_id, isbn)
            elif choice == 5:
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to return: ")
                log("Return Book", user_id=user_id, isbn=isbn)
                checkout_manager.return_book(library, user_manager, user_id, isbn)
            elif choice == 6:
                filename = input("Enter filename: ")
                log("Save Data", filename=filename)
                library.save_to_json(filename)
                user_manager.save_to_json(filename)
                print("Data saved.")
            elif choice == 7:
                filename = input("Enter filename: ")
                log("Load Data", filename=filename)
                library.load_from_json(filename)
                user_manager.load_from_json(filename)
            elif choice == 8:
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
