from django.shortcuts import render
from django.http import HttpResponse
from . models import Book

# Create your views here.
def books(request):
    books = Book.objects.all()

    output = []
    for book in books:
        output.append(f"{book.title} by {book.author}")
    
    return HttpResponse(output)
 