import json

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Checkout:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn

    def __str__(self):
        return f"User ID: {self.user_id}, ISBN: {self.isbn}"

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")

    def return_book(self, isbn):
        for i, book in enumerate(self.books, start=1):
            if book.isbn == isbn:
                del self.books[i-1]
                print(f"Book {book} returned.")
                return
        print("Book not found.")

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f)

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            if isinstance(data, list) and all(isinstance(book, dict) for book in data):
                self.books = [book.Book(**book) for book in data]
            else:
                print("Invalid data format, ignoring file.")

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, user_id):
        self.users.append((name, user_id))

    def list_users(self):
        if not self.users:
            print("No users in the library.")
            return
        for i, (name, user_id) in enumerate(self.users, start=1):
            print(f"{i}. {name} (ID: {user_id})")

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.users, f)

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            if isinstance(data, list) and all(isinstance(user, tuple) and len(user) == 2 for user in data):
                self.users = [(name, user_id) for name, user_id in data]
            else:
                print("Invalid data format, ignoring file.")

class CheckoutManager:
    def __init__(self):
        self.checkouts = []

    def checkout_book(self, library, user_manager, user_id, isbn):
        if not any(isbn == book.isbn for book in library.books):
            print("Book not found.")
            return
        if not any(user_id == user[1] for user in user_manager.users):
            print("User not found.")
            return
        for checkout in self.checkouts:
            if checkout.user_id == user_id and checkout.isbn == isbn:
                print("Book is already checked out.")
                return
        for i, book in enumerate(library.books, start=1):
            if book.isbn == isbn:
                self.checkouts.append(Checkout(user_id, isbn))
                del library.books[i-1]
                print(f"Book {book} checked out.")
                return
        print("Book not found.")

    def return_book(self, library, user_manager, user_id, isbn):
        for checkout in self.checkouts:
            if checkout.user_id == user_id and checkout.isbn == isbn:
                library.return_book(isbn)
                self.checkouts.remove(checkout)
                print("Book returned.")
                return
        print("Book not checked out.")