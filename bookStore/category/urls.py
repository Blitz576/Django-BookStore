from django.urls import path
from .views import *

urlpatterns = [
 path('',index,name='index'),
 path('<int:id>',categoryDetails,name='categoryDetails'),
 path ('addBook' ,addCategory , name='addCategory'),
 path('<int:id>/delete', deleteCategory , name='deleteCategory'),
 path('<int:id>/update',updateCategory,name='updateCategory'),
]