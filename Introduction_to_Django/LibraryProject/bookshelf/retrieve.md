<!-- Command: Retrieve and display all attributes of the book you just created.
Document in: retrieve.md
Expected Documentation: Include the Python command and a comment with the expected output showing the details of the book. -->


book = Book.objects.all().values()

print(book.id, book.title, book.author, book.publication_year)
# Expected Output: 1 1984 George Orwell 1949