from django.shortcuts import render,redirect
from .models import Article
# Create your views here.
def index(request):
    #게시글 목록 조회해서 템플릿에 전달
    #1. 게시글 목록 DB에서 조회
    #    ORM 이용해야 하는데 >> 이 역할을 Model class(Article)가 수행
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }

    return render(request,'articles/index.html',context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    # 요청에서 데이터 받아와서 DB에 저장하고
    title = request.POST.get('title')
    content = request.POST.get('content')
    # Article.objects.create()
    article = Article(title=title,content=content)
    article.save()
    
    return redirect('articles:index')

def delete(request,pk):

    # DB에서 삭제하고 목록조회해서 템플릿에 전달
    # record 단위는 instance로 처리...
    article = Article.objects.get(pk=pk)
    article.delete()
    # articles = Article.objects.all()
    # context = {
    #     'articles' :articles
    # }
    # return render(request,'articles/index.html', context)
    return redirect('articles:index')

# 상세 페이지를 보여달라는 요청을 처리하는 함수
# url에 작성한 variable routing 변수명(pk)과 동일하게
def detail(request,pk):
    # DB에서 pk에 해당하는 게시글 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request,'articles/detail.html', context)


# pk번 글의 수정 화면 보여달라는 요청을 처리하는 함수
def edit(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/update.html',context)