from django.urls import path
from .views import index,about,contact,bookDetails


urlpatterns = [
 path('index',index,name='index'),
 path('about',about,name='about'),
 path('contact',contact, name='contact'),
 path('<int:id>', bookDetails , name='bookDetails')
]