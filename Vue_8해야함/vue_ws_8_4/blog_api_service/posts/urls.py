from django.urls import path
from . import views

urlpatterns = [
    path('',views.category),
    path('category/', views.category),
    path('posts/', views.posts),
  
]
