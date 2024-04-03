from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
import json

from .models import Book

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "no_of_pages": 218,
        "author": "F. Scott Fitzgerald",
        "price": 10.99,
        "image": "one.jpg"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "no_of_pages": 281,
        "author": "Harper Lee",
        "price": 12.50,
        "image": "two.jpg"
    },
    {
        "id": 3,
        "title": "1984",
        "no_of_pages": 328,
        "author": "George Orwell",
        "price": 9.99,
        "image": "three.jpg"
    },
    {
        "id": 4,
        "title": "1984",
        "no_of_pages": 328,
        "author": "George Orwell",
        "price": 9.99,
        "image": "four.jpg"
    },
]

# def index(request):
#     return render(request, 'mainApp/index.html', context={'books': books})


def index(request):
    books_queryset = Book.objects.all()
    print(books_queryset)
    books_list = [{'id': book.id, 'title': book.title, 'no_of_pages': book.no_of_pages,
                   'author': book.author, 'price': book.price, 'image': book.image} for book in books_queryset]
    return HttpResponse(json.dumps(books_list), content_type='application/json')


def about(request):
    return render(request, 'mainApp/about.html')

def contact(request):
    return render(request, 'mainApp/contact.html')

def bookDetails(request, id):
    book_id = int(id)
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'mainApp/bookDetails.html', {'book': book})

