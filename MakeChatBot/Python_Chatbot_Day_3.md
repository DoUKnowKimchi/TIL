# Day3 웹 프레임워크 flask




### 그전에 하는, c9.io
***

​    `ctrl+shift+i` 인스펙터에서 `network` 클릭 후 `f5`를 눌러 새로 고침하면 리스트 중 첫번째 파일을 눌렀을 때, header에 보면 ip 주소가 나타난다.

이 ip는 server의 ip를 나타내는데, 이를 dns 에서 해석 후 돌려준다.


c9은 aws가 인수했는데, c9으로 서버를 웹상에서 구축, 운영 할 수 있다.

이것저것을 만들고 나서~

- 웹의 기본은 Request 와 Response로 나뉘게 된다.
- cd / 에서 /는 root directory를 의미한다.
- 주로 root 는 window os 에서 c드라이브를 의미한다.
- linux command syntax 에서 cd ~ 는 home으로 이동.


***
### URL 의 의미


  ![이미지 이름](https://qph.fs.quoracdn.net/main-qimg-33dba2957048c9c3060d575d92c83f42)

     - https://www.naver.com : 누구에게 보낼 지 (요청 받는 사람의 주소)
     - / : 가장 기본이 되는 (root) 페이지 req
     - /XXX : 무엇을 받을지
- 공부를 할 때 사용자의 입장 뿐만 아니라 제작자, server의 입장에서도 생각 해 보기.
- ex) https://search.naver.com/search.naver?where=nexearch&query=%EB%8C%80%EC%84%B1%EA%B3%A0&sm=top_lve&ie=utf8
    - SubDomain 은 다른 서버일 수도 있다.

- /search.naver : 네이버에게 검색 req
- ?XX : 여기서 XX는 parameter
    - ex)chat_id=123456789&text=hello
- ?query=XXX : 이런 단어를 담아 보낼테니 XXX를 검색 req
***
### Flask를 사용 해 보자
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"
```
"/" 이런식으로 라우팅 되는 것은 static routing이라고 한다.
그러나 사용자에게 정보를 받고 나타내는 것을 dynamic routing 이라고 한다.

```
@app.route("/hello/<name>")
def hi(name):
    return 'Hello %s' % name
```
***
 url 에서 \<var> 에 속한 값을 넣어주고 링크 이동을 하면 variable routing을 할 수 있다.

 여기서 return value는 type이 string이여야 한다. 
 ```
 # /reverse/hello ==> 
@app.route("/reverse/<msg>")
def reverse(msg):
    return msg[::-1]

# /palindrome
@app.route("/palindrome/<text>")
def palindrome(text):
    pal_text = text[::-1]
    if text == pal_text:
        return 'true'
    else :
        return 'false'
 ```
 ***
HTML 문서를 만들 때 SEO 를 생각해서 만들어야 한다. 

즉 H1과 등등을 남발하면 안되고
TITLE을 잘 작성해야 할 뿐만 아니라 

Meta tag와 tag들 또한 아름답고 이쁘게 사용해야 한다.

***
ubuntu 에서 c9.io 에 들어가서 서버를 실행하기 위한 코드는
```
flask run --host=0.0.0.0 --port=8080
```
***
```
@app.route("/profile")
def profile():
    return send_file('profile.html')
```
파이썬에서 static web 만드는 방법
return 으로 send_file(html파일 이름)
***
### 그렇다면 Dynamic web을 구현하는 방법은 무엇이 있을까?
 - template engine 사용
 - flask와 같이 쓸 수 있는것은?
 - jinja
 - return 에 render를 해줘야 한다.
 ```
    from flask import Flask, send_file, render_template
    import random as rd

    app = Flask(__name__)

    @app.route("/lotto")
    def lotto():
    result = str(sorted(rd.sample(range(1, 46), 6)))
    return render_template('lotto.html', result=result)
```
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <h1>로또 자동 생성기</h1>
        <h2>{{ result }}</h2>
    </body>
</html>
```
