from django.contrib import admin
from . models import Article
# Register your models here.
# 관리자 페이지에서 내가만든 앱 보기 -> 여기다 등록

admin.site.register(Article)