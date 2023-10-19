from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Music, Comment
from .serializers import MusicListSerializer, MusicSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MusicListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete': f'데이터 {music_pk}번 음악이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        


@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serialzier = CommentSerializer(instance = comments, many = True)
    return Response(data = serialzier.data, status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def comment_detail(request,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method == 'GET':
        serialzier = CommentSerializer(instance=comment)
        return Response(data= serialzier.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serialzier = CommentSerializer(instance=comment, data=request.data)
        if serialzier.is_valid(raise_exception=True):
            serialzier.save()
            return Response(data=serialzier.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete' : f'댓글{comment_pk}번이 삭제되었습니다.'
        }
        return Response(data,status.HTTP_204_NO_CONTENT)
    


@api_view(['POST'])
def comment_create(request,music_pk):
    music = get_object_or_404(Music,pk=music_pk)
    comment = CommentSerializer(instance=music,data=request.data)
    if comment.is_valid(raise_exception=True):
        comment.save(music=music)
        return Response(data=comment.data, status=status.HTTP_201_CREATED)
    

