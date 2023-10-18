from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


# 게시글 목록, 게시글 작성
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 요청이 들어오면 내가 가지고 있는 게시글 목록을
        articles = Article.objects.all()
        # 문자열(JSON)로 만들어서 응답
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
        # DB에 있는 게시글 가져오기 : Model
        # 파이썬 객체를 JSON 문자열로 변환 해주는 Serializer (Django가 가지고있음)
        # DRF : Model + Serializer = ModelSerializer
    
    elif request.method == 'POST':
        # 게시글 DB에 넣어주기
        # modelform과 유사한 방법으로
        serializer = ArticleSerializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE',])
def article_detail(request,article_pk):
    article = Article.objects.get(pk = article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(instance = article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
