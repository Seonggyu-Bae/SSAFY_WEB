from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('profile/<username>/', views.profile, name='profile'),

    # 팔로잉 하거나 취소하거나
    path('<int:user_pk>/follow/',views.follow, name='follow'),
]
