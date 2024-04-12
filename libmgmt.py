class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook (self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def delBook (self, book):
        self.books.remove(book)
        self.noBooks = len(self.books)
    
    def showInfo(self):
        print(f"The no. of books in library are {self.noBooks} and the books are :")
        for book in self.books:
            print(book)

l1 = Library()

l1.addBook("Harry Potter 1")
l1.addBook("Harry Potter 2")
l1.addBook("Harry Potter 3")
l1.addBook("Harry Potter 4")
l1.addBook("Harry Potter 5")
l1.addBook("Harry Potter 6")
l1.addBook("Harry Potter 7")
l1.showInfo()