from django.shortcuts import render
from django.http import HttpResponse
from . models import Book
from . models import Library
from django.views.generic import DetailView

# Create your views here.
def books(request):
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html',{"books":books})


class BookDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.book_set.all()
        return context