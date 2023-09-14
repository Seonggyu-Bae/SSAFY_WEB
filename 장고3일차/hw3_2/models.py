from django.db import models

# Create your models here.

# 조건을 참고하여 'title', 'content' 필드를 가지고 있는 Article model을 작성하시오
# 1. title의 길이 제한은 15입니다.
# 2. content의 길이 제한이 없습니다.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()