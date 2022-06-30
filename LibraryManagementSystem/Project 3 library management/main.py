class Library:
    def __init__(self, listOfBooks):
       self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books available in the library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print (f"You have been issued {bookName}. Please keep it safe. Return it within 30 days.")
            self.books.remove(bookName)
            return True
        
        else:
            print("Sorry! This book has already be issued to someone else. Please wait until the book is returned.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning the book.Hope you enjoyed reading it.Have a great day ahead!!!")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
    
if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django", "Python", "HTML", "CSS" ])
    student = Student()
    #centraLibrary.displayAvailableBooks() 

    while(True):
            welcomeMsg = '''*=*=*Welcome To Central Library*=*=* 
            Please select an option:
            1. List of all the Books
            2. Request a book
            3. Return a book
            4. Exit the library
            '''  
            print(welcomeMsg)
            
            a = int(input("Enter a choice: "))
            if a == 1:
               centraLibrary.displayAvailableBooks()     
            
            elif a == 2:
                centraLibrary.borrowBook(student.requestBook())
            
            elif a == 3:
               centraLibrary.returnBook(student.returnBook())

            elif a == 4:
                print("Thanks for using this Library.Visit again!")
                exit()
            else:
                print("Invalid Choice")

            