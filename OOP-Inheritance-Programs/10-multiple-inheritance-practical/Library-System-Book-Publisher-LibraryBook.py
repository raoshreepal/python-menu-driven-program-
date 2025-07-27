class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Publisher:
    def __init__(self, publisher_name):
        self.publisher_name = publisher_name

class LibraryBook(Book, Publisher):
    def __init__(self, title, author, publisher_name, isbn):
        Book.__init__(self, title, author)
        Publisher.__init__(self, publisher_name)
        self.isbn = isbn

    def show(self):
        print(f"'{self.title}' by {self.author}, ISBN: {self.isbn} | Publisher: {self.publisher_name}")

# Object
book = LibraryBook("Python Mastery", "Kunal Jain", "TechBooks", "978-93-12345-67-8")
book.show()
