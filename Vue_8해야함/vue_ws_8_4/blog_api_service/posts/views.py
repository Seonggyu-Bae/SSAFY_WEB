from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import PostListSerializer, PostSerializer , CategoryListSerializer, CategorySerializer
from .models import Post, Category
# Create your views here.

@api_view(['GET'])
def posts(request):
  if request.method == 'GET':
        posts = get_list_or_404(Post)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

  # elif request.method == 'POST':
  #     serializer = PostSerializer(data=request.data)
  #     if serializer.is_valid(raise_exception=True):
  #         # serializer.save()
  #         serializer.save(user=request.user)
  #         return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def category(request):
      if request.method == 'GET':
            categorys = get_list_or_404(Category)
            serializer = CategoryListSerializer(categorys, many=True)
            return Response(serializer.data)
      elif request.method == 'POST':
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                  # serializer.save()
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)