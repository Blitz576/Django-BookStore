from django.db import models
from django.shortcuts import reverse
from category.models import Category
# Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    no_of_pages = models.IntegerField(default=0)
    price = models.IntegerField()
    image = models.ImageField(upload_to='books/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null=True , related_name='books')
    def __str__(self):
        return f'{self.title}'

    @property
    def get_absolute_url(self):
        return f"/media/{self.image}"

    @property
    def delete_url(self):
        return reverse('deleteBook', args=[self.id])

    @property
    def get_edit_url(self):
        return reverse('updateBook', args=[self.id])
