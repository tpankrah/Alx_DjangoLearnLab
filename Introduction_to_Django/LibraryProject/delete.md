<!-- Delete:

Command: Delete the book you created and confirm the deletion by trying to retrieve all books again.
Document in: delete.md
Expected Documentation: Include the Python command and a comment with the expected output confirming the deletion.

 -->


from bookshel.models import Book

book = Book.objects.first()
book.delete()

print(Book.objects.all())
# Expected Output: <QuerySet []>   # confirms the book was deleted
