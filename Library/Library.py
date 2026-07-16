#Question
"""
Develop a Library Management System using functions, lists.
 The program should allow the user to add books, display all books, search for a book, issue and return books,
 and maintain book details using appropriate Python data structures.
 Use separate functions for each operation and implement a menu-driven interface.
"""
library=[]
issued=[]
def add_book():
    n=int(input("Enter the number of books: "))
    for i in range(n):
        book=input("Enter the book name: ")
        library.append(book)
    print("Books added successfully")

def display_books():
    if len(library)==0:
        print("No books found")
    else:
        print("Book List:")
        for book in library:
            print(book)
    print()

def search_book():
    book=input("Enter the book name: ")
    if book in library:
        print("Book found successfully")
    else:
        print("Book not found")

def issue_book():
    num=int(input("Enter the Number of books: "))
    for i in range(num):
        book=input("Enter the book name: ")
        if book in library:
            print("Book issued successfully")
            issued.append(book)
            library.remove(book)
        else:
            print("Book not found")

def return_book():
    book=input("Enter the book name: ")
    if book in issued:
        issued.remove(book)
        library.append(book)
        print("Book returned successfully")
    else:
        print("Book not found")
while True:
    print("-----------MENU-----------------")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    print("--------------------------------")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        add_book()
    elif choice == 2:
        display_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        issue_book()
    elif choice == 5:
        return_book()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
