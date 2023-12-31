# Django Form



## 1. 개요

**HTML 'form'**

- 지금까지 사용자로부터 데이터를 받기위해 활용한 방법

- 그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음
  
  - 따라서 유효한 데이터인지에 대한 확인이 필요



**유효성 검사**

- 수집한 데이터가 정확하고 유효한지 확인하는 과정

- 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함

- 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용



## 2. Django Form

**Django Form**

- 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구
  
  - 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공



**Django Widgets**

- **HTML 'input' element의 표현을 담당**

- widget은 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것





## 3. Django ModelForm

**Form**

- 사용자 입력 데이터를 DB에 저장하지 않을 때 (ex. 로그인)



**ModelForm**

- 사용자 입력 데이터를 DB에 저장해야 할 때 (ex. 게시글, 회원가입)

- Model과 연결된 Form을 자동으로 생성해주는 기능을 제공 (Form + Model)



**Meta class**

- ModelForm의 정보를 작성하는 곳

- ' fields' 및 'exclude' 속성
  
  - exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음



**is_valid()**

- 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환

- 모델 필드에는 기본적으로 빈 값은 허용하지 않는 제약조건이 설정 되어 있음

- **따러서 빈 값은 is_valid()에 의해 False로 평가되고 form 객체에는 그에 맞는 에러 메시지가 포함되어 다음 코드로 진행됨**



**save()**

- 데이터베이스 객체를 만들고 저장



## 4. Handling HTTP requests
