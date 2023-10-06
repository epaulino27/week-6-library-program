library_books = [] #can also do this like the gaming project

def add_book(title, author): #adds a book
    book = {
        "title": title,
        "author": author,
        "availability": True
    }
    return library_books.append(book), print("You have added the book, " + "'" + title + "'" + ", by " + author + ", to the library.")

def borrow_book(title): #makes availability false
    for book in library_books:
        if book["title"] == title and book["availability"] == True: #if there is that title and it is available
            book["availability"] = False #book no longer available because you just borrowed it
            return book["availability"], print("You have checked out the book, '" + title + "'.") #book is borrowed
        else:
            return print(title + " is unavailable to be checked-out.") #book not found or not available

def return_book(title): #changes availability back to true
    for book in library_books:
        if book["title"] == title and book["availability"] == False: #if there is that title and it is checked-out
            book["availability"] = True #book now available because you returned it
            return book["availability"], print(title + " has been returned.") #book returned
        else:
            return  print(title + " has already been returned.") #book has already been returned

def find_book(title): #finds and prints details of that book
    for book in library_books:
        if title in book["title"]: #stuck on this part
            print(book["title"], book["author"], book["availability"])
        else:
            print(title + " is not in the library.")
    return

def display_books():
    print(library_books)
    return