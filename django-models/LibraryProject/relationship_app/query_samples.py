from relationship_app.models import Author, Library

library = Library.objects.get(name = library_name)
print(library.books.all())