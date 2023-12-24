 
---


### 블로그 글 작성 주제 선정 

**주제 1.
    넷플릭스 : 넷플릭스는 영화의 평점과 후기를 앱에서 보여주지 않기 때문에 사람들이 직접 검색해서 후기를 찾아볼 것이다**
    

    problem
    1. movie 명이 영어로 되있어서 한글로 번역해야하는데 단순 번역이 안맞음
    2. 같은 이름을 가진 영화들의 전처리 필요
    3. 사진을 같이 업로드해야함
    --- 영화 블로그는 정교한 분석을 필요로하고 같은 영화 이름을 처리하거나 사진을 찾는 것이 어려움

**주제 2.
    음식 : 현재 사람들이 많이 주문하는 음식들의 효능 및 부작용을 작성하는 블로그글**  

1. 식품 크롤링하여 선택
   
```bash
problem
        1. 쿠팡 > 식품 >  과일 탭에서 쿠팡 추천 랭킹순  -> 쿠팡 웹페이지 런타임 오류 
        2. 쿠팡 웹페이지 런타임 오류 -> 마켓컬리 
        3. 마켓컬리도 크롤링은 막아놓은 듯 .. 재접속이나 페이지 이동시 런타임 오류 현상 발생
        4. 네이버 쇼핑 -> 품목의 이름이 너무 복잡함 ex) 40년 단감 태추단감 감 부유 고당도 대봉 홍시 진영단감 선물세트..
```
   
        
**11번가로 크롤링 결정**

    problem
           ex) ['[최종가5,900원]해물오꼬노미야끼', '밀키트', '2인분'] ['최종', '해물', '꼬', '노미', '끼', '밀', '키트', '인분']
           >>> 키워드를 뽑는 알고리즘을 뽑아 내야함 
           방법 1. 상세 페이지 내에서 나온 단어 수를 count 하여 중요도 결정 및 그래프를 보며 알고리즘 수정 // 예외가 너무 많음...

2. 이름, 이미지 크롤링
```bash
해당품목 키워드로 나무위키 검색 설정 (역시나 이미지 추출은 어려움)
```

3. 이름 -> chatgpt로 script 생성

4. 블로그에 script, 이미지 적용
```bash
이미지가 없는 경우 history.csv를 확인해서 다시 반복하도록 설정
```
5. script내에서 tag 추출, tag 적용

6. 업로드



### 블로그 글 chatgpt openai로 생성
    chatgpt의 openai의 토큰이 쉽게 넘어가 유료 플랜을 사용해야함 -> pyautogui로 직접 사용

### 생성된 글을 티스토리 블로그에 작성
    https://jamis.tistory.com/


### 추후 블로그 성장률에 따른 글 작성 방법 수정
    이미지, 전처리 과정 보수 필요


### 후기
    이미지 캡쳐로 조금 난잡하지만 그래도 생각하던 것으로 작동하는 무언가를 만들어서 좋았고 추후 발전시킬 여지가 많다
