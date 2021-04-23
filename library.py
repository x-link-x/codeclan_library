library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

# TODO - Print welcome statement including library name
print(f"Hello! Welcome to the {library['name']}")

option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? \n")

    library_books = library["books"]

    if option == "1":
        print("Listing all books...")
        # TODO - List all books
        for book in library_books:
            print(f"{book['title']} by {book['author']}")

    if option == "2":
        print("Searching for a book by title...")
        # TODO - Search for a book by title
        title = input("Enter a book title \n")
        message = ""
        
        for book in library_books:
            if book["title"] != title:
                continue
            message += f"We have {book['title']} by {book['author']}"
        
        if message == "":
            print("Sorry, we don't have that book right now")
        else:
            print(message)

    if option == "3":
        print("Adding a book...")
        # TODO - Add a book
        title = input("Enter the title \n")
        author = input("Enter the author \n")
        library_books.append({"author": author, "title": title})
        print("Success!")

    if option == "4":
        print("Removing a book...")
        # TODO - Remove a book
        title = input("Enter the title you wish to remove \n")
        message = ""
        
        for book in library_books:
            if book["title"] != title:
                continue
            library_books.remove(book)
            message += "Success!"
        
        if message == "":
            print("Sorry, that book is not in the database. Please try again")
        else:
            print(message)

    if option == "5":
        print("Updating a book...")
        # TODO - Update a book
        book_titles = []
        old_title = input("Enter the title to be updated \n")
        
        for book in library_books:
            book_titles.append(book["title"])  
        
        if old_title not in book_titles:
            print("Sorry, that book is not in the database. Please try again") 
        else:
            new_title = input("Enter the new title \n")
            new_author = input("Enter the new author \n")
            
            if new_title == "" or new_author == "":
                break
            
            for book in library_books:
                if book["title"] != old_title:
                    continue
                else:
                    book["title"] = new_title
                    book["author"] = new_author
                    print("Success!")