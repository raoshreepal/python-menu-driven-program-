class LibraryItem:
    def get_fine(self, days):
        pass

class Book(LibraryItem):
    def get_fine(self, days):
        return days * 2

class Magazine(LibraryItem):
    def get_fine(self, days):
        return days * 1

items = [Book(), Magazine()]
for item in items:
    print(item.get_fine(5))
