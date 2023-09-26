from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)


# new 와 create를 합침으로서 완벽한 CREATE 완성
def create(request):
    # 만약 요청의 메서드가 POST 라면 create 로직
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # 빈 값은 허용하지 않음
            # 유효성 검사가 통과됨
            article = form.save()
            return redirect('articles:detail', article.pk)
        
    # 아니라면(POST가 아니라면) new로직
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)



    
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
        # save 메서드가 생성과 수정을 구분하는 방법은
        # 객체의 키워드 인자 instance 여부를 통해 판단함
        # 있으면 수정으로 인지함
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'article' : article,
        'form' : form
    }

    return render(request, 'articles/update.html', context)
