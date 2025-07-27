class Book:
    def __init__(self, title):
        self.title = title

class BorrowedBook(Book):
    def __init__(self, title, borrower):
        super().__init__(title)
        self.borrower = borrower

class OverdueBook(BorrowedBook):
    def __init__(self, title, borrower, days_late):
        super().__init__(title, borrower)
        self.days_late = days_late

    def info(self):
        print(f"'{self.title}' borrowed by {self.borrower} | Overdue: {self.days_late} days")

# Object
b = OverdueBook("Atomic Habits", "Nidhi", 5)
b.info()
