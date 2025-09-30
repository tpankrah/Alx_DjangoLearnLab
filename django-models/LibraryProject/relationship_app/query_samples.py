from relationship_app.models import Author, Library, Book, Librarian

library = Library.objects.get(name=library_name)
print(library.books.all())

author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
print(books.all())


librarian = Librarian.objects.get(library=)
print(librarian)