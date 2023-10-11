# 23/10/11



## Many to one relationship



### 1. 개요

**Many to one relationships (N:1 or 1:N)**

- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계

- Comment(N) - Article(1) : 0개 이상의 댓글은 1개의 게시글에 작성될 수 있다.



**ForeignKey()**

- N:1 관계 설정 모델 필드



### 2. 댓글 모델 구현

**댓글 모델 정의**

- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 **단수형**으로 작성하는 것을 권장

- ForeignKey 클래스를 작성하는 위치와 관계없이 외래 키는 테이블 필드 마지막에 생성됨

- ```python
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      content = models.CharField(max_length=200)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```



**ForeignKey(to, on_delete)**

- to : 참조하는 모델 class 이름

- on_delete : 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정(데이터 무결성)

- on_delete가 'CASCADE' 라면 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제





### 3. 관계 모델 참조

**역참조**

- N:1 관계에서 1에서 N을 참조하거나 조회하는 것 (1 -> N)

- N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만 1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 이름이 필요

- 모델인스턴스.역참조이름(related manager).QuerySetAPI -> article.comment_set.all()



**related manager**

- N:1 혹은 M:N 관계에서 역참조시에 사용하는 매니저

- 'objects' 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨



**related manager 이름 규칙**

- N:1 관계에서 생성되는 Related manager의 이름은 참조하는 "모델명_set"이름 규칙으로 만들어짐

- 해당 댓글의 게시글(Comment -> Article)
  
  - comment.article

- 게시글의 댓글 목록(Article -> Comment)
  
  - article.comment_set.all()







### 4. 댓글 구현



**댓글 CREATE 구현**



**댓글 READ 구현**



**댓글 DELETE 구현**




