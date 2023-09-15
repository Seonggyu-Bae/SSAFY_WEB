from django.urls import path
from . import views

# url을 이름으로 가져다 쓸때
# 명확하게 구분하기 위해서
# 이름공간을 지정

app_name ='articles'
# articles의 throw
# anotherapp 의 throw는 다른거니까

urlpatterns = [
    path('throw/', views.throw, name = 'throw'), # 사용자가 서버로 데이터를 전달하기 위한 화면
    path('catch/', views.catch, name = 'catch'), # 전달된 데이터를 받아서 보여주는 화면
]
