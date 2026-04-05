class Library:

    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def checkout(self):
        if self.available:
            self.available = False
            print(self.book_name, "checked out.")
        else:
            print("Book not available.")

    def return_book(self):
        self.available = True
        print(self.book_name, "returned.")

    def display(self):
        if self.available:
            print(self.book_name, "by", self.author, "is available.")


book1 = Library("Python Basics", "John")
book2 = Library("Data Structures", "Smith")

book1.display()
book1.checkout()
book1.return_book()
