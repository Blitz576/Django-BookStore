from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'