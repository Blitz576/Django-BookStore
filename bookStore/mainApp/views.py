from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
import json

from .models import Book
from .forms import BookForm
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
   # print(books_queryset)
    return render(request, 'mainApp/index.html', {'books': books_queryset})

def about(request):
    return render(request, 'mainApp/about.html')

def contact(request):
    return render(request, 'mainApp/contact.html')

def bookDetails(request, id):
    book_id = int(id)
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'mainApp/categoryDetails.html', {'book': book})



def addBook(request):
    book = BookForm()
    if request.method == 'POST':
        book = BookForm(request.POST, request.FILES)
        if book.is_valid():
           book.save()
           return redirect('index')
    return render(request, 'mainApp/addCategory.html', {'form': book})

def deleteBook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('index')
def updateBook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        if request.method == 'POST':
            bookForm = BookForm(request.POST, request.FILES)
            if book.is_valid():
                book.save()
                return redirect('index')
    return render(request, 'mainApp/updateCategory.html', {'book': book})






# using native html


# def addBook(request):
#     if request.method == 'POST':
#         if request.FILES:
#             image = request.FILES["image"]
#         else:
#             image = None
#         print(request.POST)
#         product = Book(title=request.POST["title"], price=request.POST["price"],
#                           author=request.POST["author"],no_of_pages=request.POST["no_of_pages"], image=image)
#         product.save()
#         return redirect('index')
#     return render(request, 'mainApp/addCategory.html')










# def updateBook(request, id):
#     book = get_object_or_404(Book, id=id)
#     if request.method == 'POST':
#         #check if there's any photoes updated or not
#         if request.FILES:
#             image = request.FILES["image"]
#         else:
#             image = book.image
#         book.title = request.POST["title"]
#         book.author = request.POST["author"]
#         book.no_of_pages = request.POST["no_of_pages"]
#         book.image = image
#
#         # saving into data base
#         book.save()
#         return redirect('index')
#     return render(request, 'mainApp/updateCategory.html', {'book': book})
