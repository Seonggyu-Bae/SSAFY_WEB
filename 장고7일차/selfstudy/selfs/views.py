from django.shortcuts import render,redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request,'selfs/index.html',context)

def create(request):
    return render(request,'selfs/create.html')

def aaa(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.POST.get('image')
    created_at = request.POST.get('created_at')
    updated_at = request.POST.get('updated_at')

    article = Article()

    article.title = title
    article.content = content
    article.image = image
    article.created_at = created_at
    article.updated_at =updated_at

    article.save()

    return redirect('selfs:detail',article.pk)

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'selfs/detail.html',context)

    return render(request,context)
def update(request,pk):
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.POST.get('image')
    updated_at = request.POST.get('updated_at')

    article = Article.objects.get(pk=pk)

    article.title = title
    article.content = content
    article.image = image
    article.updated_at =updated_at

    article.save()

    return redirect('selfs:detail',article.pk)

def edit(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'selfs/edit.html',context)

def delete(request,pk):
    pass