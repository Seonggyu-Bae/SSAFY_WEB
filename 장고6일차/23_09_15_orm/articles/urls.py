from django.urls import path
from . import views
app_name='articles'
urlpatterns = [
    # index, new, create, delete
    path('index/',views.index, name='index'),
    path('new/',views.new, name='new'),
    path('create/',views.create, name='create'),
    path('delete/<int:pk>/',views.delete, name='delete'),
    # 상세 페이지 /articles/pk/
    path('<int:pk>/',views.detail, name='detail'),
    # 수정 페이지
    # 수정 화면을 보여줘
    path('edit/<int:pk>/', views.edit, name='edit'),

    # 수정해


]