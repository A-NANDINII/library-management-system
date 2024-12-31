from src.books import search_books, borrow_book

# Test the search_books function
results = search_books("Gatsby")
print("Search Results:", results)

# Test the borrow_book function
borrow_book("1234567890", "user01")
