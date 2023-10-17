from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    # 게시글이 userModel을 참조한다 -> 게시글을 작성한 사용자를 참조하기 위해서
    # Article.user = 게시글 작성자
    # User.article_set 내가 작성한 게시글 목록을 보려면 역참조(ModelName.??_set)를 해야함
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    )
    # 게시글 입장에서 좋아요를 누른 user 정보를 가지고 있는것이다.
    # Article.like_users: 이 게시글을 좋아요 한 사용자
    # User.like_articles : 사용자가 좋아요를 누른 게시글들
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,  related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
