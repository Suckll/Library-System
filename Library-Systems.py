


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_book = {}

    def remove_book(self, book):
        for i in self.books:
            if i.title == book.title:
                self.books.remove(i)

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("\n")
        print("Books available in library\n")
        for book in self.books:
            book.display_books()

    def add_members(self, member):
        self.members.append(member)

    def remove_members(self, member):
        self.members = [m for m in self.members if m.name != member.name]

    def display_members(self):
        for member in self.members:
            member.display_members()
        print("\n")
        print("Members in library\n")

    def borrowed_books(self,book,member):
        for i in self.books:
            if i.title == book.title:
                if i in self.borrowed_book:
                    print("\n")
                    print(f"Book {i.title} is already borrowed\n")
                else:
                    self.borrowed_book[i] = member
                    print("\n")
                    print(f"Book {i.title} is now borrowed by {member.name}\n")
                return
            print("\n")
            print("Book not found in the library.\n")

    def display_borrowed_books(self):
        for book, member in self.borrowed_book.items():
            print("\n")
            print(f"Book: {book.title}, Member: {member.name}\n")

    def remove_borrowed_book(self,book):
        if book in self.borrowed_book:
            self.borrowed_book.pop(book)
        else:
            print("\n")
            print("Book not found.")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def update_book(self, update_title, update_author):
        self.title = update_title
        self.author = update_author

    def display_books(self):
        print("\n")
        print(f"Title: {self.title}, Author: {self.author}\n")

    def borrowed_books(self):
        print("\n")
        print(f"Title: {self.title}, Author: {self.author}\n")

class Member:
    def __init__(self, name, member_id, age):
        self.name = name
        self.member_id = member_id
        self.age = age

    def add_member(self, update_name, update_id, update_age):
        self.name = update_name
        self.member_id = update_id
        self.age = update_age

    def display_members(self):
        print("\n")
        print(f"Name: {self.name}, ID: {self.member_id}, Age: {self.age}\n")


#test
library = Library()
library.add_members(Member("You", "1", "20"))
library.add_book(Book("Book1", "Author1"))
#Remove from here! if you dont want user input
print("""
.____    ._____.                                 _________                    __
|    |   |__\\_ |______________ _______ ___.__.  /   _____/__.__. ______ _____/  |_  _____
|    |   |  || __ \\_  __ \\__  \\\\_  __ <   |  |  \\_____  <   |  |/  ___// __ \\   __\\/     \\ 
|    |___|  || \\_\\ \\  | \\// __ \\|  | \\/\\___  |  /        \\___  |\\___ \\\\  ___/|  | |  Y Y  \\
|_______ \\__||___  /__|  (____  /__|   / ____| /_______  / ____/____  >\\___  >__| |__|_|  /
        \\/       \\/           \\/       \\/              \\/\\/         \\/     \\/           \\/
""")



print("\n")
initialize = input("Press Enter to start \n")


print("\n")
print("Welcome to the library management system!\n")
print("type 'exit' to exit")
print("1. Add Book")
print("2. Remove Book")
print("3. Display Books")
print("4. Add Member")
print("5. Remove Member")
print("6. Display Members")
print("7. Borrow Book")
print("8. Return Book")
print("9. Display Borrowed Books")

while True:
    print("\n")
    choice = input("Enter your choice: \n")

    if choice == "0":
        print("\n")
        print("Welcome to the library management system!\n")
        print("Type 'exit' to exit")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Add Member")
        print("5. Remove Member")
        print("6. Display Members")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Display Borrowed Books")
        print("\n")

    if choice.lower() == "exit":
        break

    if choice == "1":
        try:
            book_input = input("Enter a book to add format ('[name] , [author]')  !\n")
            book_details = book_input.split(",")
            title = book_details[0].strip()
            author = book_details[1].strip()
            book = Book(title, author)
            book_exists = False
            for i in library.books:
                if i.title == book.title and i.author == book.author:
                    book_exists = True
                    break
            if book_exists:
                print("\n")
                print("Book already exists in the library.\n")
            else:
                library.add_book(book)
                print("\n")
                print("Book added successfully\n")
        except IndexError:
            print("\n")
            print("Invalid input format. Please enter the book details in the format '[name] , [author]'.\n")

    if choice == "2":
        try:
            print("\n")
            book_input = input("Enter a book to remove format '[name] , [author]'  !\n")
            book_details = book_input.split(",")
            title = book_details[0].strip()
            author = book_details[1].strip()
            book = Book(title, author)
            for i in library.books:
                if i.title == book.title:
                    library.remove_book(book)
                    print("\n")
                    print("Book removed successfully\n")
                    break
            else:
                print("\n")
                print("Book not found in the library.\n")
        except IndexError:
            print("\n")
            print("Invalid input format. Please enter the book details in the format '[name] , [author]'.\n")

    if choice == "3":
        if len(library.books) == 0:
            print("\n")
            print("No books in the library.\n")
        else:
            library.display_books()

    if choice == "4":
        try:
                print("\n")
                member_input = input("Enter a member to add format '[name] , [id] , [age]'  !\n")
                member_details = member_input.split(",")
                name = member_details[0].strip()
                member_id = member_details[1].strip()
                age = member_details[2].strip()
                member = Member(name, member_id, age)
                member_exists = False
                for i in library.members:
                    if i.member_id == member.member_id:
                        member_exists = True
                        break
                if member_exists:
                    print("\n")
                    print("Member already exists in the library.\n")
                else:
                    library.add_members(member)
                    print("\n")
                    print("Member added successfully\n")
        except IndexError:
            print("\n")
            print("Invalid input format. Please enter the member details in the format '[name] , [id] , [age]'.\n")


    if choice == "5":
        try:
            print("\n")
            member_input = input("Enter a member to remove format '[name] , [id] , [age]'  !\n")
            member_details = member_input.split(",")
            name = member_details[0].strip()
            member_id = member_details[1].strip()
            age = member_details[2].strip()
            member = Member(name, member_id, age)
            member_found = False
            for existing_member in library.members:
                if (existing_member.name == member.name and existing_member.member_id == member.member_id and existing_member.age == member.age):
                    library.members.remove(existing_member)
                    print("\n")
                    print("Member removed successfully\n")
                    member_found = True
                    break
            if not member_found:
                print("\n")
                print("Member not found in the library.\n")
        except IndexError:
            print("\n")
            print("Invalid input format. Please enter the member details in the format '[name] , [id] , [age]'.\n")

    if choice == "6":
        if len(library.members) == 0:
            print("\n")
            print("No members in the library.\n")
        else:
            library.display_members()

    if choice == "7":
        try:
            print("\n")
            member_input = input("Enter a member to borrow a book format '[name] , [id] , [age]'  !\n")
            member_details = member_input.split(",")
            name = member_details[0].strip()
            member_id = member_details[1].strip()
            age = member_details[2].strip()
            member = Member(name, member_id, age)
            member_found = False
            for existing_member in library.members:
                if (existing_member.name == member.name and
                    existing_member.member_id == member.member_id and
                    existing_member.age == member.age):
                    member_found = True
                    break

            if not member_found:
                print("\n")
                print("Member not found in the library.\n")
                continue

            library.display_books()
            book_input = input("Enter a book to borrow format '[name] , [author]'  !\n")
            book_details = book_input.split(",")
            title = book_details[0].strip()
            author = book_details[1].strip()
            book = Book(title, author)
            book_found = False
            for existing_book in library.books:
                if existing_book.title == book.title and existing_book.author == book.author:
                    book_found = True
                    break

            if book_found:
                library.borrowed_books(book, member)
                library.remove_book(book)

            else:
                print("\n")
                print("Book not found in the library.\n")
        except IndexError:
            print("\n")
            print("Invalid input format. Please enter the book details in the format '[name] , [author]'.\n")

    if choice == "9":
        if len(library.borrowed_book) == 0:
            print("\n")
            print("No borrowed books in the library.\n")
        else:
            library.display_borrowed_books()

    if choice == "8":
        try:
            print("\n")
            member_input = input("Enter a member to return a book format '[name] , [id] , [age]'  !\n")
            member_details = member_input.split(",")
            name = member_details[0].strip()
            member_id = member_details[1].strip()
            age = member_details[2].strip()
            member = Member(name, member_id, age)
            member_found = False
            for existing_member in library.members:
                if (existing_member.name == member.name and
                    existing_member.member_id == member.member_id and
                    existing_member.age == member.age):
                    member_found = True
                    break

            if not member_found:
                print("\n")
                print("Member not found in the library.\n")
                continue

            library.display_borrowed_books()
            book_input = input("Enter a book to return format '[name] , [author]'  !\n")
            book_details = book_input.split(",")
            title = book_details[0].strip()
            author = book_details[1].strip()
            book = Book(title, author)
            book_key = f"{title}, {author}"

            for book, member in library.borrowed_book.items():
                if book.title == book.title and book.author == book.author:
                    library.remove_borrowed_book(book)
                    library.add_book(book)
                    print("\n")
                    print("Book returned successfully\n")
                    break
                else:
                    print("\n")
                    print("Book not found in the library.\n")
        except  IndexError:
            print("\n")
            print("Invalid input format. Please enter the book details in the format '[name] , [author]'.\n")

print("\n")
print("Thank you for using our library management system. Goodbye!")

