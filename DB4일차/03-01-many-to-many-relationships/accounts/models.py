from django.db import models
from django.contrib.auth.models import AbstractUser
from articles.models import Article



# Create your models here.
class User(AbstractUser):
    # like_article = models.ManyToManyField(Article, related_name='like_users')     
    following = models.ManyToManyField('self',symmetrical=False, related_name = 'followers')