## 1. Framework?

- #### 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
  
  (개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공)



## 왜 프레임워크를 사용할까?

- #### 기본적인 구조, 도구, 규칙 등을 제공하기 때문에 개발자는 필수적인 핵심 개발에만 집중 할 수 있음

- #### 여러 라이브러리를 제공해 개발 속도를 빠르게 할 수 있음(생산성)

- #### 유지보수와 확장에 용이해 소프트웨어의 품질을 높임



# 2. 클라이언트와 서버



## 웹의 동작 방식



### 클라이언트(Client)?

- #### 서비스를 요청하는 주체
  
  (웹 사용자의 인터넷이 연결된 장치, 웹브라우저)

### 서버(Server)?

- #### 클라이언트의 요청에 응답하는 주체(웹 페이지, 앱을 저장하는 컴퓨터)



### 우리가 웹 페이지를 보게 되는 과정

1. 웹 브라우저(클라이언트)에서 google.com을 입력

2. 브라우저는 인터넷에 연결된 전세계 어딘 가에 있는 구글 컴퓨터(서버)에게 Google홈페이지 html 파일을 달라고 요청

3. 요청을 받은 구글 컴퓨터는 DB에서 html 파일을 찾아 응답

4. 전달받은 html파일을 웹 브라우저가 사람이 볼 수 있도록 해석해주면서 사용자는 구글의 메인 페이지를 보게 됨



## 3. 프로젝트 및 가상환경



### 가상환경

- #### Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 <mark>독립적인 </mark>실행 환경



- 서로 다른 프로젝트에서 다른 패키지 버전 사용을 위해 독립적인 개발환경이 필요

- 서로 다른 프로젝트에서 패키지 충돌을 피하기 위해 독립적인 개발 환경이 필요



### 가상환경 venv 생성 명령어

- python -m venv venv

### 가상환경 활성화

- source venv/Scripts/activate

### 환경에 설치된 패키지 목록 확인

- pip list





### 의존성 패키지

- #### 한 소프트웨어 패키지가 다른 패키지의 기능이나 코드를 사용하기 때문에 그 패키지가 존재해야만 제대로 작동하는 관계

- #### 사용하려는 패키지가 설치되지 않았거나, 호환되는 버전이 아니면 오류가 발생하거나 예상치 못한 동작을 보일 수 있음




### 의존성 패키지 관리의 중요성

- 개발환경에서난 각각의 프로젝트가 사용하는 패키지와 그 버전을 정확히 관리하는 것이 중요











# Django 프로젝트와 앱



## Django project?

- #### 애플리케이션의 집합 ( DB 설정, URL 연결, 전체 앱 설정 등을 처리 )



## Django application?

- #### 독립적으로 작동하는 기능 단위 모듈 (각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성)



##### EX) 만약 커뮤니티 카페를 만든다면

- **프로젝트 : 카페(전체 설정담당)**

- **앱 : 게시글, 댓글, 회원 관리 등 (DB, 로직, 화면)**



# Django 디자인 패턴



## 디자인 패턴?

- ### 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책 ( 공통적인 문제를 해결하는데 쓰이는 형식화 된 관행)



## MVC 디자인 패턴?

- ### (Model, View, Controller)

- ### 애플리케이션을 구조화하는 대표적인 패턴 (데이터, 사용자 인터페이스, 비즈니스 로직을 분리)

- ### 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위해



## MTV 디자인 패턴

- ### (Model, Template, View)

- ### Django에서 애플리케이션을 구조화하는 패턴 ( 기존 MVC 패턴과 동일하나 명칭을 다르게 정의한 것)

- ### View -> Template, Controller - > View









# 요청과 응답





## 데이터 흐름에 따른 코드 작성

- ### URLs -> View -> Template


