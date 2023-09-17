# 웹 소개



**Web**

- Web site, Web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술



**Web site**

- 인터넷에서 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간



**Web page**

- HTML, CSS 등의 웹 기술을 이용하여 만들어진, **"Web site"를 구성하는 하나의 요소**



**Web page 구성 요소**

- HTML : "Structure"

- CSS : "Styling"

- Javascript : "Behavior"



# 웹 구조화



**HTML**

- HyperText Markup Language

- 웹 페이지의 의미와 **구조**를 정의하는 언어



**Hypertext**

- 웹 페이지를 다른 페이지로 연결하는 링크

- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트



**Markup Language**

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

- EX) HTML, Markdown



# HTML 구조



**<!DOCTYPE html>**

- 해당 문서가 html 문서라는 것을 나타냄



**<html></html>**

- 전체 페이지의 콘텐츠를 포함



**<title></tittle>**

- 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용



**<head></head>**

- HTML 문서에 관련된 설명, 설정 등

- 사용자에게 보이지 않음



**<body></body>**

- 페이지에 표시되는 모든 컨텐츠



**HTML Element(요소)**

- 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨

- 닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재



**HTML Attributes(속성)**

- 속성은 요소 이름과 속성 사이에 공백이 있어야 함

- 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함

- 속성 값은 열고 닫는 따옴표로 감싸야 함

- 나타내고 싶지 않지만 **추가적인 기능, 내용**을 담고 싶을 때 사용

- CSS에서 해당 **요소를 선택**하기 위한 값으로 활용됨



# Text Structure



HTML의 주요 목적 중 하나는 **텍스트 구조와 의미**를 제공하는 것



**대표적인 HTML Text Structure**

- **Heading & Paragraphs**
  
  - h1 ~ h6, p

- **Lists**
  
  - ol, ul, li

- **Emphasis & Importance**
  
  - em, strong





# CSS



**CSS (Cascading Style Sheet)**

- 웹 페이지의 **디자인과 레이아웃**을 구성하는 언어



```html
h1 { h1: 선택자(Selcetor)
    color: red;    #선언(Declaration)
    font-size: 30px;
     #속성      #값
   (Property)   (Value)
}
```



**CSS 적용 방법**

- 인라인(inline) 스타일
  
  - HTML 요소 안에 style 속성 값으로 작성

- 내부 스타일 시트
  
  - head 태그 안에 style 태그에 작성

- 외부 스타일 시트
  
  - 별도의 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기



# CSS 선택자



**CSS Selectors**

- HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자



**CSS Selectors 종류**

- **기본 선택자**
  
  - **전체(*) 선택자**
    
    - HTML 모든 요소를 선택
  
  - **요소(tag) 선택자**
    
    - 지정한 모든 태그를 선택
  
  - **클래스(class) 선택자 ('.' (dot))**
    
    - 주어진 클래스 속성을 가진 모든 요소를 선택
  
  - **아이디(id) 선택자 ('#')**
    
    - 주어진 아이디 속성을 가진 요소 선택
    
    - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
  
  - 속성(attr) 선택자 등

- **결합자(Combinators)**
  
  - **자손 결합자 (" "(space) )**
    
    - 첫 번째 요소의 자손 요소들 선택
    
    - 예) p span은 <p>  안에 있는 모든 <span>을 선택 (하위 레벨 상관 없이)
  
  - **자식 결합자(>)**
    
    - 첫 번째 요소의 직계 자식만 선택
    
    - 예) ul > li 는 <ul> 안에 있는 모든 <li>를 선택 (한단계 아래 자식들만)



**우선순위**

- 동일한 요소에 적용 가능한 같은 스타일을 두 가지 이상 작성 했을 때 어떤 규칙이 적용 되는지 결정하는 것

- **Cascade (계단식)**
  
  - 동일한 우선순위를 같는 규칙이 적용될 때 **CSS에서 마지막에 나오는 규칙**이 사용됨



**우선순위가 높은 순**

1. **Importance**
   
   - !important

2. **Inline 스타일**

3. **선택자**
   
   - id 선택자 > class선택자 > 요소 선택자

4. **소스 코드 순서**



# CSS상속



**기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임**



**상속여부**

- **상속 되는 속성**
  
  - Text 관련 요소(font, color, text-align), opactity, visibility 등

- **상속 되지 않는 속성**
  
  - Box model 관련 요소(width, height, border, box-sizing)
  
  - position 관련 요소(position, top/right/bottom/left, z-index) 등
