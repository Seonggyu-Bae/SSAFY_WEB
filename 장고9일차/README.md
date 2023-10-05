# 23/10/05

## Django Authentication System 2



### 1. 회원 가입



**회원 가입**

- User 객체를 Create 하는 과정

**UserCreationForm()**

- 회원 가입시 사용자 입력 데이터를 받을 built-in ModelForm

- 장고 기본 유저 모델을 사용하기 때문에 그대로 사용하게 되면 개발자가 대체한 커스텀 유저 모델이 적용되지 않아 오류가 발생함 -> 커스텀 유저 모델을 사용하려면 커스텀Form을 작성해주어야 함



**get_user_model()** : django.contrib.auth 에 있음

- 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환하는 함수

- Django는 User 클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 필수적으로 강조하고 있음





### 2. 회원 탈퇴

**회원 탈퇴**

- User 객체를 Delete 하는 과정



### 3. 회원정보 수정

**회원정보 수정**

- User 객체를 Update 하는 과정



**UserChangeForm()**

- 회원정보 수정 시 사용자 입력 데이터를 받을 built-in ModelForm

- User 모델의 모든 정보들(fields)까지 모두 출력되어 수정이 가능하기 때문에 일반 사용자들이 접근해서는 안되는 정보는 출력하지 않도록 해야 함

- 따라서 CustomUserChangeForm을 만들어 접근 가능한 필드를 조정



수정이기에 **instance인자**가 들어가야함





### 4. 비밀번호 변경

**비밀번호 변경**

- 인증된 사용자의 **Session 데이터를 Update** 하는 과정



**PasswordChagneForm()**

- 비밀번호 변경 시 사용자 입력 데이터를 받을 built-in Form



**세션 무효화 방지하기**

- **비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게** 되어버리기 때문에 로그인 상태가 유지되지 못하고 로그아웃  처리가 된다.

- **update_session_auth_hash(request, user)**
  
  - **암호 변경 시 세션 무효화를 막아주는 함수**
  
  - 암호가 변경되면 새로운 password의 Session Data로 기존 Session을 자동으로 갱신







### 5. 로그인(인증된) 사용자에 대한 접근 제한



**1. is_authenticated**

- 사용자가 인증되었는지 여부를 알 수 있는 User model의 속성
  
  - 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성, 비인증 사용자에 대해서는 항상 False



**2. login_required**

- **인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터(@)**
  
  - 비인증 사용자의 경우 /accounts/login/ 주소로 redirect 시킴


