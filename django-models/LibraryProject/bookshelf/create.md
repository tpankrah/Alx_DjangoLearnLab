<!-- Command: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.
Document in: create.md
Expected Documentation: Include the Python command and a comment with the expected output noting the successful creation -->

from bookshelf.models import Book

book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = "1949")

print(book.id, book.title, book.author, book.publication_year)
# Expected Output: 1 1984 George Orwell 1949