from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# 전체 게시글 조회
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


# 단일 게시글 조회
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

# 
def new(request):
    return render(request, 'articles/new.html')

def create(request):
   
    title = request.POST.get('title')
    content = request.POST.get('content')
    # DB에 저장하는 1번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # DB에 저장하는 2번째 방법
    article = Article(title = title, content = content)
    article.save()

     # DB에 저장하는 3번째 방법
    # Article.objects.create(title = title, content = content)

    # return render(request, 'articles/create.html')
    return redirect('articles:index')

def delete(request, pk):
    # 몇 번 게시글을 삭제할 것인가?
    article = Article.objects.get(pk=pk)
    # 조회한 게시글을 삭제
    article.delete()

    return redirect('articles:index')


def edit(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
   
    title = request.POST.get('title')
    content = request.POST.get('content')
   
    article = Article.objects.get(pk = pk)
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail',article.pk)