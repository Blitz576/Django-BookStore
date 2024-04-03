from django.urls import path
from .views import index,about,contact,bookDetails
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 # path('index',index,name='index'),
 # path('about',about,name='about'),
 # path('contact',contact, name='contact'),
 # path('<int:id>', bookDetails , name='bookDetails'),
 # path('books', bookList, name='bookList')

 path('',index,name='index'),
 path('about',about,name='about'),
 path('contact',contact,name='contact'),
 path('<int:id>',bookDetails,name='bookDetails')


]