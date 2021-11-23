class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" * " + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Plaease keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issueed to someone else. Please wait until the book is available.")
            return False

    def returnBook(self, bookName):
        if bookName == "" or " ":
            print("Enter Valid Name.")
        else:
            self.books.append(bookName)
            print("Thanks for returning this book! Hope you enjoyed reading it.")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the bok you want to return: ")
        return self.book

if __name__ == "__main__":
    centerlibrary = Library(["Algorithms", "Django", "Clrs", "Python"])
    student = Student()
    while(True):
        welcomeMsg ='''
 ===== Welcome to central Library =====
        Please choose an option:
        1. Listing all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the library
        '''
        print(welcomeMsg)
        a = int (input("Enter a choice : "))
        if a == 1 :
            centerlibrary.displayAvailableBooks()
        elif a == 2:
            centerlibrary.borrowBook(student.requestBook())
        elif a == 3:
            centerlibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing central library. having a great day ahead!")
            exit()
        else: 
            print("Invalid Choice!")
            
        
