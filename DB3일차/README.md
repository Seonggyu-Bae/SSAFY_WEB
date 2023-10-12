# Many to one relationships 2

## 1. 개요

 **Article(N) - User(1)**

- 0개 이상의 게시글은 1명의 회원에 의해 작성 될 수 있다.

**Comment(N) - User(1)**

- 0개 이상의 댓글은 1명의 회원에 의해 작성 될 수 있다.

## 2. Article & User

### 모델관계설정

**Article - User 모델 관계 설정**

- User 외래 키 정의

- ```python
  from django.conf import settings
  
  class Article(models.Model):
      # 모델관계 설정 (모델을 직접참조하지 않음)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      # settings.AUTH_USER_MODEL 으로 USER model을 참조
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

**User 모델을 참조하는 2가지 방법** : '내부적인 구동 순서'와 '반환 값'에 따른 이유

- **get_user_model()**
  
  - 반환 값 : User Object (객체)
  
  - 사용위치 : **models.py가 아닌 다른 모든 위치**

- **settings.AUTH_USER_MODEL**
  
  - 반환 값 : accounts.User (문자열)
  
  - 사용위치 : **models.py**

- **User 모델은 직접 참조하지 않는다!**

**Migration**

**게시글 CREATE**

1. 기존 ArticleForm 출력 변화 확인
   
   1. user 모델에 대한 외래 키 데이터 입력을 위해 불필요한 input(User선택창)이 출력

2. ArticleForm 출력 필드  수정
   
   ```python
   class ArticleForm(forms.ModelForm):
       class Meta:
           model = Article
           # fields = ('title','content',)
           exclude = ('user',)
   ```

3. 게시글 작성 시 에러 발생
   
   1. user_id 필드 데이터가 누락되었기 때문

4. 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용
   
   ```python
   @login_required
   def create(request):
       if request.method == 'POST':
           form = ArticleForm(request.POST)
           if form.is_valid():
               # 아래 3줄이 수정된 부분
               article = form.save(commit=False)
               article.user = request.user
               article.save()
               return redirect('articles:detail', article.pk)
       else:
           form = ArticleForm()
       context = {
           'form': form,
       }
       return render(request, 'articles/create.html', context)
   ```

**게시글 READ**

1. 각 게시글의 작성자 이름을 출력하기위해 html 파일 수정

**게시글 UPDATE**

1. 게스글 수정 요청 사용자와 게시글 작성 사용자를 비교하여 본인의 게시글만 수정 할 수 있도록 하기

```python
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 사용자 비교 
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid:
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    # 게시글 수정 요청 사용자와 게시글 작성 사용자가 다르면 메인페이지로 이동
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

2. 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 html파일 수정(DTL if문 사용)

**게시글 DELETE**

1. 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제 할 수 있도록 하기

```python
@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')
```

## 3. Comment & User

**Comment - User 모델 관계 설정**

- User 외래 키 정의

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # Comment - User 모델 관계 설정
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- Migration시 Article과 User모델 관계 설정 때와 동일하게 기본 값 설정 과정이 필요

**댓글 CREATE**

- 댓글 작성 시 이전에 게시글 작성 할 때와 동일한 에러 발생
  
  - 댓글의 user_id 필드 데이터가 누락되었기 때문

- 댓글 작성 시 작성자 정보가 함께 저장될 수 있도록 작성

```python
@login_required
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        # 댓글을 다는 유저는 현재 유저이다.
        comment.user = request.user
        comment_form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

**댓글 READ**

- 댓글 출력 시 댓글 작성자와 함께 출력
  
  - html에서 DTL 태그 추가

**댓글 DELETE**

- 댓글 삭제 요청 사용자와 댓글 작성 사용자를 비교하여 본인의 댓글만 삭제 할 수 있도록 하기

```python
@login_required
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # 댓글 삭제 요청자와 댓글 작성 사용자가 같다면
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
```

- 해당 댓글의 작성자가 아니라면, 댓글 삭제 버튼을 출력하지 않도록 함
  
  - html의 if DTL태그이용





참조



키 : 레코드를 구분할 수 있는 속성, 속성집합





후보키, 기본키



후보키 : 레코드를 구분할 수 있는 속성집합중 크기가 가장 작은 놈들

기본키 : 후보키 중에 하나 정함?












