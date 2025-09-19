<!-- Command: Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.
Document in: update.md
Expected Documentation: Include the Python command and a comment with the expected output showing the updated title. -->

from bookshelf.models import Book

book = Book.objects.first()
book.title = “Nineteen Eighty-Four”
book.save()


print(book.id, book.title, book.author, book.publication_year)
# Expected Output: 1 Nineteen Eighty-Four George Orwell 1949
