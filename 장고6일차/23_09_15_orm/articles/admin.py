from django.contrib import admin
from .models import Article
# Register your models here.
# 관리자 페이지에서 Article 보고 싶다...보여줘
class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.get_fields()]
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title','content','create_at','update_at']
admin.site.register(Article,ArticleAdmin)

