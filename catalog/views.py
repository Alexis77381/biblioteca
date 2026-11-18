from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(view_request):
    books = Book.objects.all()  # Obtenemos todos los libros de la base de datos
    return render(view_request, 'catalog/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'catalog/book_detail.html', {'book': book})