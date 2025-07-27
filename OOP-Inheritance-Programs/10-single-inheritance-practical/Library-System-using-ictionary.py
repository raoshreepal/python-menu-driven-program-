class Book:
    def __init__(self, title, author, info):
        self.title = title
        self.author = author
        self.info = info  # dictionary {‘pages’: 300, ‘year’: 2020}

    def get_info(self):
        for key in self.info:
            print(f"{key.capitalize()}: {self.info[key]}")

class DigitalBook(Book):
    def show(self):
        print(f"Book: {self.title} by {self.author}")
        self.get_info()

db = DigitalBook("Python Basics", "John", {"pages": 250, "year": 2022})
db.show()
