# main.py
import books
import members
#import functions

def display_menu():
    print("\nLibrary Management System")
    print("----------------------------")
    print("1. Add a new book to the library.")
    print("2. Register a new library member.")
    print("3. Borrow a book.")
    print("4. Return a book.")
    print("5. Display all books.")
    print("6. Display all members.")
    print("7. Exit.")
    print("----------------------------")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1": #adds a book
            t = input("What is the title of the Book?")
            a = input("What is the author of the Book?")
            books.add_book(t,a)
            pass
        elif choice == "2": #registers new member
            n = input("What is the name you are registering?")
            members.register_member(n)
            pass
        elif choice == "3": #borrow book
            t = input("What is the title of the Book?")
            books.borrow_book(t)
            pass
        elif choice == "4":
            t = input("What is the title of the Book?")
            books.return_book(t)
            pass
        elif choice == "5":
            books.display_books() #display all books
            pass
        elif choice == "6":
            members.display_members() #display all members
            pass
        elif choice == "7":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()

