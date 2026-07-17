# Library Manager

def get_menu_choice():

    print("Main Menu")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Quit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 5:
                break
            print("Choice must be between 1 and 5.")
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5")

    return choice

def add_book(books):
    book_title = input("What is the title of the book? ")
    book_author = input("Who is the author of the book? ")

    for book in books:
        if book["Title"] == book_title and book["Author"] == book_author:
            print("Book already exists.")
            return

    book_dict = {"Title": book_title, "Author": book_author}
    books.append(book_dict)
    print("Book added!")

def view_books(books):
    if len(books) == 0:
        print("No books yet.")
    else:
        for book in books:
            print(f"Title: {book['Title']}\nAuthor: {book['Author']}")

def search_book(books):
    if len(books) == 0:
        print("No books yet.")
        return

    book_to_search = input("What is the name of the book? ")

    for book in books:
        if book["Title"] == book_to_search:
            print(f"Title: {book['Title']}\nAuthor: {book['Author']}")
            return

    print("Book not found.")

def remove_book(books):
    if len(books) == 0:
        print("No books yet.")
        return

    book_to_delete = input("What is the name of the book? ")

    for book in books:
        if book["Title"] == book_to_delete:
            books.remove(book)
            print("Book removed!")
            return
    print("Book not found.")

def main():
    books = []

    while True:
        choice = get_menu_choice()
        if choice == 1:
            add_book(books)
        elif choice == 2:
            view_books(books)
        elif choice == 3:
            search_book(books)
        elif choice == 4:
            remove_book(books)
        elif choice == 5:
            break

main()