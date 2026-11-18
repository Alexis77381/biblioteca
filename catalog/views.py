from django.shortcuts import render
from .models import Book

def book_list(view_request):
    books = Book.objects.all()  # Obtenemos todos los libros de la base de datos
    return render(view_request, 'catalog/book_list.html', {'books': books})