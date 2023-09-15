from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # auto_now_add : 처음 작성되는 시기만 저장하고 그 후에는 안함
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now : 건드릴때마다 업데이트함
    updated_at = models.DateTimeField(auto_now=True)