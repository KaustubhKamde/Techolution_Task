class Checkout:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn

    def __str__(self):
        return f"User ID: {self.user_id}, ISBN: {self.isbn}"