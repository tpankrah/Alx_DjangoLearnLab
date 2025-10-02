from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books

urlpatterns = [
    path('books/',list_books, name='books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

]