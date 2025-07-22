class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.issued_copies = 0

    def issue(self):
        if self.issued_copies < self.total_copies:
            self.issued_copies += 1
            print(f"Issued '{self.title}' successfully.")
        else:
            print(f"No copies of '{self.title}' left.")

    def display(self):
        available = self.total_copies - self.issued_copies
        print(f"Title: {self.title} by {self.author}")
        print(f"Available Copies: {available}")

# Usage
book1 = Book("Python Basics", "John Doe", 5)
book1.issue()
book1.issue()
book1.display()
