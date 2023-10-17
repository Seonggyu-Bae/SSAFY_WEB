### 1. user.article_set 역참조 매니저 충돌

1. like_users 필드 생성 시 자동으로 역참조 .article_set 매니저가 생성됨

2. 그러나 이전 N:1(Article-User) 관계에서 이미 같은 이름의 매니저를 사용 중
   
   1. user.article_set.all() ->  해당 유저가 작성한 모든 게시글 조회

3. 'user가 작성한 글(user.article_set)'과 'user가 좋아요를 누른 글 (user.article_set)'을 구분할 수 없게 됨

4. 따라서 user와 관계된 ForeignKey 혹은 ManyToManyField 둘 중 하나에 **related_name 작성 필요**



### 2. remove와  add의 위치가 반대로 되어있었음 아래 코드가 정답

```python
@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
```



### 3.  조회자와 조회할사람이 같으면 못하게 설정 하고 폼도 안뜨게함

```python
# accounts/views.py

@require_POST
@login_required
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
        # if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
```

```html
{% if request.user != person %}
    <div>
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if user in person.followers.all %}
          <button>Unfollow</button>
        {% else %}
          <button>Follow</button>
        {% endif %}
      </form>
    </div>
    {% endif %}
```


