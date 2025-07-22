class Library:
    def __init__(self):
        self.books = []  # List to hold all book records

    def add_book(self, title, author, copies):
        book = {
            "title": title,
            "author": author,
            "copies": copies
        }
        self.books.append(book)

    def display_books(self):
        print("\n--- Library Books ---")
        count=0
        for book in self.books:
            
            print("-------------------")
            print(f" Enter Book details {count}")
            print(f"Title: {book['title']}, Author: {book['author']}, Copies: {book['copies']}")
            count+=1

# Usage
lib = Library()
n = int(input("Enter number of books to add: "))

for i in range(n):
    print("-------------------")
    print(f" Enter Book details {i}")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    copies = int(input("Enter number of copies: "))
    lib.add_book(title, author, copies)

lib.display_books()
