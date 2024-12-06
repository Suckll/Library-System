
# Library Management System

## Overview

The **Library Management System** allows users to manage books and members in a library. This system supports various functionalities such as adding/removing books and members, displaying the list of books and members, and borrowing/returning books. It is a command-line based interface that helps users interact with the library system and perform necessary operations.

## Features

- **Add a Book**: Adds a new book to the library collection.
- **Remove a Book**: Removes an existing book from the library collection.
- **Display Books**: Displays all available books in the library.
- **Add a Member**: Adds a new member to the library.
- **Remove a Member**: Removes an existing member from the library.
- **Display Members**: Displays all library members.
- **Borrow a Book**: Allows a member to borrow a book.
- **Return a Book**: Allows a member to return a borrowed book.
- **Display Borrowed Books**: Displays a list of all borrowed books and their corresponding members.

## Classes

### 1. **Library**
This class manages the core functionality of the library, such as adding/removing books and members, and handling borrowed books.

#### Methods:
- `add_book(book)`: Adds a book to the library.
- `remove_book(book)`: Removes a book from the library.
- `display_books()`: Displays all books available in the library.
- `add_member(member)`: Adds a member to the library.
- `remove_member(member)`: Removes a member from the library.
- `display_members()`: Displays all members of the library.
- `borrowed_books(book, member)`: Allows a member to borrow a book.
- `remove_borrowed_book(book)`: Removes a book from the borrowed list.

### 2. **Book**
Represents a book in the library with a title and an author.

#### Methods:
- `update_book(title, author)`: Updates the title and author of a book.
- `display_books()`: Displays the details of the book.

### 3. **Member**
Represents a library member with a name, member ID, and age.

#### Methods:
- `add_member(name, member_id, age)`: Updates the member's name, ID, and age.
- `display_members()`: Displays the details of the member.

## Usage

1. **Starting the Program**: Run the program to interact with the library system.
2. **Main Menu**: After starting, you will be prompted with a menu where you can choose an action:
   - Add or remove books.
   - Add or remove members.
   - Borrow or return books.
   - Display the list of books and members.
3. **Input Format**: Follow the input format shown when prompted (e.g., `name, author` for books, `name, id, age` for members).
4. **Exit the Program**: Type `exit` to quit the program.

## Example

```plaintext
Welcome to the library management system!
type 'exit' to exit
1. Add Book
2. Remove Book
3. Display Books
4. Add Member
5. Remove Member
6. Display Members
7. Borrow Book
8. Return Book
9. Display Borrowed Books
```

You can interact with the program by entering the corresponding number for the desired action.

## Installation

To run this program, you only need Python installed. Clone the repository and execute the Python file in a terminal:

```bash
git clone https://github.com/YourUsername/Library-System.git
cd Library-System
python library_system.py
```

## Requirements

- Python 3.x or above

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
