from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):

    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id','title',)

    # override (댓글 조회 시 게시글 번호만 제공해주는 것이 아닌 게시글 제목까지 제공해보자)

    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)

# 특정 필드를 override 혹은 추가한 경우 read_only_fields는 동작하지 않음
# 해당 필드의 read_only 키워드 인자로 작성해야함

class ArticleSerializer(serializers.ModelSerializer):
   
    # class CommentSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Comment
    #         fields = ('id','content')

    # 역참조 데이터 구성
    # 단일 게시글 조회시 해당 게시글에 작성된 댓글 목록 데이터, 댓글 개수 데이터도 함께 붙여서 응답
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'