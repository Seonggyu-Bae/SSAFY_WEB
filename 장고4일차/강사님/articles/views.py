from django.shortcuts import render,redirect
from .models import Article
# Create your views here.

def index(request):
    # 게시글 목록 조회해서 템플릿에 전달
    # 1. 게시글 목록 DB에서 조회
    # ORM을 이용해야하는데 >> model class (Article)이 역할을 수행함
    # - > import
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html',context)

def new(request):

    return render(request, 'articles/new.html')

def create(request):
    # 요청에서 데이터 받아서 DB에 저장하고
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:index')

def delete(request,pk):
    # DB에서 데이터 삭제후
    # record 단위는 instance로 처리
    article = Article.objects.get(pk=pk)
    article.delete()
    
    return redirect('articles:index')