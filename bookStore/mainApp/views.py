from django.http import HttpResponse
from django.shortcuts import render


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

def index(request):
    return render(request, 'mainApp/index.html',context={'books':books})


def about(request):
    return render(request, 'mainApp/about.html')

def contact(request):
    return render(request, 'mainApp/contact.html')

def bookDetails(request,id):
    for book in books:
        if book['id'] == id:
            print(book)
            return render(request, 'mainApp/bookDetails.html',context={"book": book})
    return HttpResponse(status=404,content_type='text/plain',body="Book not found")
