from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article,Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # 댓글작성하는 Form
    comment_form = CommentForm()
    # 특정 게시글의 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()

    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

def comments_create(request,pk):
    # 게시글 조회를 해야함 (어떤 게시글에 댓글을 다는지 알아야하니까)
    article = Article.objects.get(pk=pk)

    # CommentForm으로 사용자의 입력 받음
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # save를 commit 하지않고 instance는 필요할때 commit=False
        comment = comment_form.save(commit=False)
        # article id 가 필요하니까
        comment.article = article
        # 저장
        comment_form.save()
        return redirect('articles:detail',article.pk)
    context = {
        'article' : article,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html',context)

def comments_delete(request, article_pk, comment_pk):
    # 게시글 조회
    comment = Comment.objects.get(pk=comment_pk)

    # url에서 article_pk를 받지않고 아래처럼 해도 된다.
    # article_pk = comment.article.pk
    comment.delete()
    return redirect('articles:detail', article_pk)
