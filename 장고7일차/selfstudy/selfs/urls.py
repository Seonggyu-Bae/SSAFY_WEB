from django.urls import path
from . import views

app_name = 'selfs'

# CRUD
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/',views.detail,name='detail'),
    path('create/', views.create, name= 'create'),
    path('aaa/', views.aaa, name= 'aaa'),
    path('update/<int:pk>/', views.update, name= 'update'),
    path('edit/<int:pk>/', views.edit, name= 'edit'),
    path('delete/',views.delete,name='delete'),
]
