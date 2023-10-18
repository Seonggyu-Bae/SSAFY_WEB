from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 게시글 조회
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(instance=articles,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    # 게시글 생성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(instance=article)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(instance=article ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pk = article_pk
        article.delete()
        return Response({'delete' : f'게시글 {pk}번이 삭제되었습니다.'},status=status.HTTP_204_NO_CONTENT)