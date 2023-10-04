# 23/10/04



## 1. Cookie & Session

**HTTP** : HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약, 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초



**HTTP 특징**

- **비 연결 지향(connectionless)**
  
  - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음

- **무상태(stateless)**
  
  - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음



**쿠키(Cookie)**

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

- 클라이언트 측에 저장되는 작은 데이터 파일이며, 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식

- 같은 서버에 다른 페이지로 재요청시마다 받고 저장해 놓았던 쿠키를 함께 전송



**쿠키 사용 원리**

1. 브라우저(클라이언트)는 쿠키를 KEY-VALUE의 데이터 형식으로 저장

2. 이렇게 쿠키를 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송
- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용
  
  - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
  
  - **상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억 시켜 주기 때문**



**쿠키 사용 목적**

1. **세션 관리(Session management)**
   
   1. 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리

2. 개인화(Personalization)
   
   1. 사용자 선호, 테마 등의 설정

3. 트래킹(Tracking)
   
   1. 사용자 행동을 기록 및 분석



**세션(Session)**

- 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지

- 상태 정보를 저장하는 데이터 저장 방식

- 쿠키에 세션 데이터를 저장하여 매 요청시마다 세션 데이터를 함께 보냄



**세션 작동 원리**

1. 클라이언트가 로그인을 하면 서버가 session 데이터를 생성 후 저장

2. 생성된 session 데이터에 인증 할 수 있는 session id를 발급

3. 발급한 session id를 클라이언트에게 응답

4. **클라이언트는 응답 받은  session id를 쿠키에 저장**

5. **클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달**

6. **쿠키는 요청 때마다 서버에 함께 전송 되므로 서버에서 session id를 확인해 로그인 되어있다는 것을 알도록 함**



**쿠키와 세션의 목적**

- 서버와 클라이언트 간의 상태를 유지



## 2. Authentication System



**Django Authentication System(인증 시스템)**

- 사용자 인증과 관련된 기능을 모아 놓은 시스템



## 3. Custom User model



**Custom User model로 대체 하기**

- django가 기본적으로 제공하는 User model은 내장된 auth 앱의 User 클래스를 사용



**User 클래스를 대체하는 이유**

- 개발자가 직접 수정하기 위해서

- Django에서 강력하게 권장함??????????

- 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 **필요한 경우 나중에 맞춤 설정이 가능하기 때문**



## 4. Login



**Login**

- Session을 Create하는 과정



**AuthenticationForm()**

- 로그인 인증에 사용할 데이터를 입력 받는 built-in form

- login(request, user) : AuthenticationForm을 통해 인증된 사용자를 로그인 하는 함수

- get_user() : AuthenticationForm의 인스턴스 메서드
  
  - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환



## 5. Logout

**Logout**

- Session을 Delete하는 과정



**logout(request)**

- 현재 요청에 대한 Session Data를 DB에서 삭제

- 클라이언트의 쿠키에서도 Session id를 삭제



## 6. Template with Authentication data



**Template with Authentication data**

- 템플릿에서 인증 관련 데이터를 출력하는 방법
