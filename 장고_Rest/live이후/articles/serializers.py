from rest_framework import serializers
from .models import Article



class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title','content','id',)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

