from django.urls import path
from .views import *

urlpatterns = [
 path('',index,name='index'),
 path('<int:id>',category_details,name='categoryDetails'),
 path ('addBook' ,add_category , name='addCategory'),
 path('<int:id>/delete', delete_category , name='deleteCategory'),
 path('<int:id>/update',update_category(),name='updateCategory'),
]