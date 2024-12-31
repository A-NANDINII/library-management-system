from src.books import load_books, save_books

def return_book(isbn, user_id):
    books = load_books()
    for book in books:
        if book['isbn'] == isbn and not book['available']:
            book['available'] = True
            save_books(books)
            print(f"Book with ISBN '{isbn}' returned successfully by user {user_id}!")
            return
    print(f"Book with ISBN '{isbn}' is not borrowed.")
