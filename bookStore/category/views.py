from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import json

from .models import Category
from .forms import CategoryForm  # Assuming CategoryForm is defined


def index(request):
    """Displays a list of all categories."""
    categories = Category.objects.all()
    return render(request, 'category/index.html', {'categories': categories})


def categoryDetails(request, id):
    category = get_object_or_404(Category, pk=id)  # Use primary key (pk) for clarity
    return render(request, 'category/categoryDetails.html', {'category': category})


def addCategory(request):
    category_form = CategoryForm(request.POST, request.FILES if request.method == 'POST' else None)

    if request.method == 'POST':
        if category_form.is_valid():
            category_form.save()
            return redirect('index')

    return render(request, 'category/addCategory.html', {'category_form': category_form})


def deleteCategory(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('index')


def updateCategory(request, id):
    category = get_object_or_404(Category, pk=id)
    category_form = CategoryForm(request.POST or None, request.FILES or None, instance=category)

    if request.method == 'POST':
        if category_form.is_valid():
            category_form.save()
            return redirect('index')

    return render(request, 'category/updateCategory.html', {'category_form': category_form})
