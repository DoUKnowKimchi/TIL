# Chatbot quest
## linux command

`cat (text)` => 어떤 것의 내용을 출력

`code .bashrc` => 현 위치에 .bashrc를 조작하는 것을 만든다.

`source .bashrc` => reload후 실행한다 .bashrc를

`echo '환경변수'` => 환경변수  출력. echo가 print 같은것.

`c9 ~/.bashrc` => c9 에서 작업시

.bashrc 에서 변수저장은
```
export TELEGRAM_TOKEN="비밀"
export NAMES="쉿"
export USERID="하하하핫"

alias TIL="cd ~//Desktop//study//TIL"
alias CHAT="cd ~//Desktop//study//chat"
alias STUDY="cd ~//Desktop//study"
```
***
## 함수 생성 로직 함수(function) => 모듈화(기능별로 분리)
### 0. 분리한다.
### 1. 입력을 무엇을 받을지 생각한다 (정한다.)
### 2. 결과가 어떻게 되는지 생각한다. (정의한다.)
### 3. 입력 -> 결과 과정을 생각한다.. (정의한다.)
***
## OpenCV (Opensource Computer Vision)

https://opencv.org/

또는 Naver Clova api 를 이용해서 뭔가를 해본다.
***
## REST API
*   GET : 가져오다. 특정 정보를 가져오다. => **default** 

    `method` 웹의 대부분  요청.
*   POST : 게시하다. 쓰다. 작성하다. 데이터를 보내다. => 글쓰기 시

    methods=['post']로 된경우 url로 접근할 시 get 방식이 되므로, get 방식으로 접근하려고 하면 method not allowed 가 나타나게 된다.
*   PATCH :
*   DELETE :
```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('') => @app.route('', methods=['get'])
def index():
    return render_template()
    
    플라스크 기본 템플릿
```
**POSTMAN** 겁내 많이 쓸 예정.
***
## **WEBHOOK**
json parsing 할 때 키로 직접 접근 할 시(인덱스 접근) 에러가 나면 파일이 멈출 수도 있다. 그래서 get으로 접근하는게 훨씬 낫다. 에러를 우회할 수 있음(None 반환. None Type)


