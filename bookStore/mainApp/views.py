from django.shortcuts import render


books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "no_of_pages": 218,
        "author": "F. Scott Fitzgerald",
        "price": 10.99,
        "image": "great_gatsby.jpg"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "no_of_pages": 281,
        "author": "Harper Lee",
        "price": 12.50,
        "image": "to_kill_a_mockingbird.jpg"
    },
    {
        "id": 3,
        "title": "1984",
        "no_of_pages": 328,
        "author": "George Orwell",
        "price": 9.99,
        "image": "1984.jpg"
    },
    # Add more books as needed
]

def index(request):
    return render(request, 'mainApp/index.html',context={'books':books})


def about(request):
    return render(request, 'mainApp/about.html')

def contact(request):
    return render(request, 'mainApp/contact.html')
