import json

BOOKS_FILE = "storage/books.json"

def load_books():
    try:
        with open(BOOKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file, indent=4)

def add_book(title, author, isbn):
    books = load_books()
    books.append({"title": title, "author": author, "isbn": isbn, "available": True})
    save_books(books)
    print(f"Book '{title}' added successfully!")

def remove_book(isbn):
    books = load_books()
    updated_books = [book for book in books if book['isbn'] != isbn]
    save_books(updated_books)
    print(f"Book with ISBN '{isbn}' removed successfully!")

def search_books(query):
    books = load_books()
    results = [book for book in books if query.lower() in book['title'].lower() or 
               query.lower() in book['author'].lower()]
    return results

def borrow_book(isbn, user_id):
    books = load_books()
    for book in books:
        if book['isbn'] == isbn and book['available']:
            book['available'] = False
            save_books(books)
            print(f"Book '{book['title']}' borrowed successfully by user {user_id}!")
            return
    print(f"Book with ISBN '{isbn}' is not available.")
