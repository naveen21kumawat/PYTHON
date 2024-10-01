class library():
    def __init__(self):
        self.books = []
        self.noBook = 0

    def addBook(self ,book):
        self.books.append(book)

    def show(self):
        print(f"Libary has {len(self.books)} Books . they are")
        for b in self.books:
            print(b)


            
B1 = library()
B1.addBook("Python")
B1.addBook("java")
B1.addBook("C++")
B1.show()  # LIbary has 3 Books . they are Python java C++
