# DATA ABSTRACTION(It hides internal (DD)details and definition,it shows (FF) Features and Functionality).
# ENCAPSULATION(Collection of variables,functions,statements that encapsulated by class).

books = ["c++", "python", "java"]


class library:
    def __init__(self, books):
        self.books = books

    def list_books(self):
        print("Available books:")
        for book in self.books:
            print(book)

    def borrow_book(self, borrow_book):
        if borrow_book in self.books:
            print("Book is available take it")
            self.books.remove(borrow_book)
        else:
            print("Book is not there")

    def receive_books(self, receive_books):
        print(" You Returned  book")
        self.books.append(receive_books)


o = library(books)

msg = ("""
1.list of books
2.borrow book
3.receive book
""")

while True:
    print(msg)
    choice = int(input("Enter the number:"))
    if choice == 1:
        o.list_books()

    elif choice == 2:
        book = input("Enter book name to borrow:")
        o.borrow_book(book)

    elif choice == 3:
        book = input("Enter book name to return:")
        o.receive_books(book)

    else:
        print("THANK YOU COME AGAIN!")
        quit()
