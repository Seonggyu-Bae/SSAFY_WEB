from django.contrib import admin
from .models import Article
# 어드민 페이지에서 모델을 확인 하려면 등록을 해야함

admin.site.register(Article)