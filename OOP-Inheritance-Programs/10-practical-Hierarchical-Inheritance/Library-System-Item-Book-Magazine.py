class Item:
    def __init__(self, title):
        self.title = title

class Book(Item):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def show(self):
        print(f"Book: '{self.title}' by {self.author}")

class Magazine(Item):
    def __init__(self, title, issue):
        super().__init__(title)
        self.issue = issue

    def show(self):
        print(f"Magazine: '{self.title}', Issue: {self.issue}")

# Objects
b = Book("The Alchemist", "Paulo Coelho")
m = Magazine("Tech Today", "July 2025")

b.show()
m.show()
