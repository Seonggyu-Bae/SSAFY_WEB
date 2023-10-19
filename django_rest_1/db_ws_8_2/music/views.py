from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Music
from .serializers import MusicListSerializer, MusicSerializer



@api_view(['GET','POST'])
def music_list(request):
    # 전체 음악 조회
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicListSerializer(instance = musics, many = True)
        return Response(data = serializer.data)
    # 음악 생성
    elif request.method =='POST':
        serializer = MusicSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, music_pk):
    music = Music.objects.get(pk=music_pk)
    
    # 상세 음악 조회
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    # 상세 음악 수정
    elif request.method == 'PUT':
        serializer = MusicSerializer(instance=music, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # 상세 음악 삭제
    elif request.method == 'DELETE':
        pk = music_pk
        music.delete()
        return Response({'delete' : f'음악{pk}번이 삭제되었습니다'}, status=status.HTTP_204_NO_CONTENT)


    