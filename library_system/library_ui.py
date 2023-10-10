# library_ui.py

import tkinter as tk
from tkinter import messagebox, simpledialog
import main  # Assuming main.py contains the functions for the library operations

import members
import books


def register_member():
    name = simpledialog.askstring("Input", "Enter the members name:")
    if name:  # Check if the user provided a name (didn't press cancel)
        members.register_member(name)  # Calls the function to register a member
        messagebox.showinfo("Success", "Member added successfully!")
    else:
        messagebox.showwarning("Warning", "Book addition cancelled. Name was not provided.")

def borrow_book():
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:  # Check if the user provided a title (didn't press cancel)
        books.borrow_book(title)  # Calls the function to borrow a book
        messagebox.showinfo("Success", "Book borrowed successfully!")
    else:
        messagebox.showwarning("Warning", "Book addition cancelled. Title was not provided.")


def return_book():
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:  # Check if the user provided a title (didn't press cancel)
        books.return_book(title)  # Calls the function to borrow a book
        messagebox.showinfo("Success", "Book returned successfully!")
    else:
        messagebox.showwarning("Warning", "Book addition cancelled. Title was not provided.")


def display_books():
    display = books.display_books() # Calls the function to display all books
    messagebox.showinfo("All Books", books.library_books) #shows user list


def display_members():
    members.display_members() # Calls the function to display all members
    messagebox.showinfo("All Members", members.library_members) #shows member list

def end_program():
    messagebox.showinfo("End Program", "Your now closing the program") #make this end the program



def add_book():
    """Capture details and add a book to the library."""
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:  # Check if the user provided a title (didn't press cancel)
        author = simpledialog.askstring("Input", "Enter the book's author:")
        if author:  # Check if the user provided an author
            books.add_book(title, author)  # Using the function from books.py
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showwarning("Warning", "Book addition cancelled. Author was not provided.")
    else:
        messagebox.showwarning("Warning", "Book addition cancelled. Title was not provided.")


root = tk.Tk()
root.title("Library Management System")

# Menu buttons
add_book_btn = tk.Button(root, text="Add a new book", command=add_book)
add_book_btn.pack(pady=10)

register_member_btn = tk.Button(root, text="Register a new member", command=register_member)
register_member_btn.pack(pady=10)

borrow_book_btn = tk.Button(root, text="Borrow a book", command=borrow_book)
borrow_book_btn.pack(pady=10)

return_book_btn = tk.Button(root, text="Return a book", command=return_book)
return_book_btn.pack(pady=10)

display_books_btn = tk.Button(root, text="Display all books", command=display_books)
display_books_btn.pack(pady=10)

display_members_btn = tk.Button(root, text="Display all members", command=display_members)
display_members_btn.pack(pady=10)

close_program_btn = tk.Button(root, text="End Program", command=end_program)
close_program_btn.pack(pady=10)

root.mainloop()