# 23/09/14



## Django Model





**Django Model**

- DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
  
  - 테이블 구조를 설계하는 '청사진(blueprint)'



**model 클래스 살펴보기**

```python
# example code
# articles/models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
```

- **작성한 모델 클래스는 최종적으로 DB에 테이블 구조를 만든다.**

- django.db.models 모듈의 Model이라는 부모 클래스를 상속받음

- Model은 model에 관련된 모든 코드가 이미 작성 되어있는 클래스
  
  - 개발자는 가장 중요한 테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록 하기 위한 것 (프레임워크의 이점)

- 클래스 변수명
  
  - 테이블의 각 "필드(열) 이름"

- model Field 클래스
  
  - 테이블 필드의 "데이터 타입"

- model Field 클래스의 키워드 인자 (필드 옵션)
  
  - 테이블 필드의 "제약조건" 관련 설정



**제약조건**

- 데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙
  
  - ex) 숫자만 저장되도록, 문자가 100자 까지만 저장되도록 하는 등의 조건





**Migrations**

- model 클래스의 변경사항(필드 생성, 수정, 삭제 등)을 DB에 최종 반영하는 방법



**Migrations 과정**

model class        --------->             migration 파일         ------->             db.sqlite3(DB)

                    (makemigrations)                                     (migrate)



**Migrations 핵심 명령어 2가지**

- python manage.py makemigrations
  
  - model class를 기반으로 최종 설계도(migration)작성

- python manage.py migrate
  
  - 최종 설계도를  DB에 전달하여 반영



**추가 Migrations**

- 이미 생성된 테이블에 필드를 추가해야 한다면?
1. 추가 모델 필드 작성

```python
# example code
# articles/models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
    # 아래가 추가된 필드
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

2. python manage.py makemigrations
- 이미 기존 테이블이 존재하기 때문에 필드를 추가 할 때 필드의 기본 값 설정이 필요

- 1번은 현재 대화를 유지하면서 직접 기본 값을 입력 하는 방법

- 2번은 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법



3.   
   
   - 추가하는 필드의 기본 값을 입력해야 하는 상황
   
   - 날짜 데이터이기 때문에 직접 입력하기 보다 Django가 제안하는 기본 값을 사용하는 것을 권장
   
   - 아무것도 입력하지 않고 enter 를 누르면 Django가 제안하는 기본 값으로 설정됨

4.  
   
   - migrations 과정 종료 후 2번째 migration 파일이 생성됨을 확인
   
   - 이처럼 Django는 설계도를 쌓아가면서 추후 문제가 생겼을 시 복구하거나 되돌릴 수 있도록 함 (마치 'git commit')

5.  
   
   - migrate 후 테이블 필드 변화 확인



                                **따라서 model class에 변경사항(1)이 생겼다면, 
                                            반드시 새로운 설계도를 생성(2)하고, 
                                                이를 DB에 반영(3)해야 한다.**

                          1. model class변경 -> 2. makemigrations -> 3. migrate





## 모델필드



**Model Field**

- DB 테이블의 필드(열)을 정의하며, 해당 필드에 저장되는 데이터 타입과 제약조건을 정의



| CharField()         | 길이의 제한이 있는 문자열을 넣을 때 사용<br/>(필드의 최대 길이를 결정하는 max_length는 필수 인자) |
|:-------------------:|:---------------------------------------------------------------:|
| **TextField()**     | 글자의 수가 많을 때 사용                                                  |
| **DateTimeField()** | 날짜와 시간을 넣을 때 사용                                                 |

- DateTimeField의 선택인자
  
  - auto_now:데이터가 **저장될 때마다** 자동으로 현재 날짜시간을 저장 (수정일)
  
  - auto_now_add:데이터가 **처음 생성될 때만** 자동으로 현재 날짜시간을 저장 (작성일)





## Admin Site



**Automatic admin interface**

- Django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공
  
  - 데이터 확인 및 테스트 등을 진행하는데 매우 유용



**admin 계정 생성**

- email은 선택사항이기 때문에 입력하지 않고 진행 가능

- 비밀번호 입력시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가기

- python manage.py createsuperuser



**admin에 모델 클래스 등록**

- **admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능**



**admin site 로그인 후 등록된 모델 클래스 확인**



**데이터 생성, 수정, 삭제 가능**





## 참고



**데이터베이스 초기화**

- 1. migration 파일 삭제
  
  2. db.sqlite3 파일 삭제

- __init__.py 및 migration 폴더 를 지우지 않도록 주의



**Migrations 기타 명령어**

- python manage.py showmigrations
  
  - migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 명렁어
  
  - X 표시가 있으면 migrate가 완료되었음을 의미

- python manage.py sqlmigrate articles 0001
  
  - 해당 migrations 파일이 SQL 언어로 어떻게 번역되어 DB에 전달되는지 확인하는 명렁어



**CRUD**

- 소프트웨어가 가지는 기본적인 데이터 처리 기능

- Create (저장)

- Read (조회)

- Update (갱신)

- Delete (삭제)
