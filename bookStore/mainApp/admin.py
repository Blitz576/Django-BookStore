from django.contrib import admin


# Import book
from .models import Book

# Register your models here.
admin.site.register(Book)