class library:
    def __init__(self):
        self.books=[]
        self.n=0
    def values(self,book):
        self.books.append(book)
        self.n=len(self.books)
    def allbooks(self):
        print(f"no of books are {self.n}")
        print("all books are")
        for i in self.books:
            print(i)
    

lib=library()
while True:
    n=int(input("enter no of book to enter: "))

    for i in range(n):
        book=input("enter book: ")
        lib.values(book)

    lib.allbooks()    

    i=int(input("enter 1 if to enter more book, 0 for exit: "))
    if i==1:
        pass
    elif i==0:
        break
    else:
        print("invalid input")
        break
