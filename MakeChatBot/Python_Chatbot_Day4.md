# Day4 Flask upgrade + templating + session + Storaging

template engine : Jinja(on Python)
HTML template 안에 파이썬 코드 {{ var }} <= 파이썬 기반 template engine

python web-framework 에서 rendering 할 때 return 값에 변수를 보내주고, 이를 HTML에서 사용 가능

Jinja 에서 조건문도 사용 가능한데, 
```
{% if site == 'web' %}
  <span>web</span>
{% elif site == 'is' %}
  <span>is</span>
{% else %}
  <span>com</span>
{% endif %}
```
이렇게 사용된다. 주의해야 할 부분은 종료시 `endif` 를 사용해야 한다는 것이다.

반복문 또한 종료시 `{% endfor %}` 처럼 종결 해야 한다.

***
c9.io에서 세팅 하는 법
- flask
  - fakesearch
    - templates
      - 뭐뭐머.html
    - `app.py`
***
`app.py` setting
```
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
```
***
webhook 확인하기 => to make sth 나중에!
***
## 틈새를이용한 jinja2 공부
***
파이썬을 위한 template language 에용!
  ### 진자특
  * sandboxed excution `sandbox` 외부 접근 및 영향을 차단하여 제한된 영역 내에서만 프로그램을 동작시키는 것
  * template inheritance
  * automatic HTML escaping system for XSS prevention
  * Just in time compile
***
## faker.python ( faker.js)
***
그 페이커가 아니다. 페이커 센빠이가 아님.

```
** app.py **

from flask import Flask, render_template, request
from faker import Faker
from random import *

app = Flask(__name__)

fake = Faker('ko_KR')

babos = []

fishes = []
num = 0
# '/'에서 사용자의 이름을 입력 받습니다.
@app.route("/")
def index():
    
    return render_template('index.html')

@app.route("/match")
def match():
    me = request.args.get('l_name')
    you = request.args.get('ld_name')
    num_rate = randint(50,100)
    fishes.append([me,you])
    
    return render_template('match.html', me=me, you=you, rate = num_rate)

@app.route("/admin")
def admin():
    return render_template('admin.html', fishes = fishes)

@app.route("/junsang")
def junsang():
    
    return render_template('junsang.html')

# '/pastlife' : 사용자의 (랜덤으로 생성된 전생을 보여준다self.)
# 당신은 
# KV로 만들어서 활용.

@app.route("/pastlife")
def pastlife():
    name = request.args.get('name')
    # past[0] : 과거이름 / [1] : 직업 / [2] 나이  / [3] 사용자의 이름 / [4] 사용자 태어난 날짜 /[5] 사용자 죽은 날짜
    past =[]
    age = randint(16,80 )
    death = randint(1500,1900)
    born = str(death - age)
    born_m = str(randint(1,12))
    born_d = str(randint(1,28))
    death_m = str(randint(1,12))
    death_d = str(randint(1,28))
    
    past.append(fake.name())
    past.append(fake.job())
    past.append(age)
    past.append(name)
    past.append(born+'년 '+born_m+'월 '+born_d +'일')
    past.append(str(death)+'년 ' + death_m+'월 '+death_d +'일')
    
    return render_template('pastlife.html', past=past)
```
`templates -> index.html`
```
  <h1>당신이 좋아하는 그 사람은 당신을 얼마나 좋아할까?</h1>
    <form action="/match">
        <label for="l_name">당신의 이름은?</label>
            <input id="l_name" type="text" name="l_name"/>
        <label for="ld_name">상대방의 이름은?</label>
            <input id="ld_name" type="text" name="ld_name" />
        <input type="submit" />
    </form>
```
`templates -> match.html`
```
  <p> {{ you }} 님이 {{ me }} 님을 좋아하는 마음은 {{ rate }} % 입니다.</p>
```
`templates -> admin.html`
```
   {% for i in fishes:  %}
                <span> {{ i }}</span>
        <br />
    {% endfor %}
```

이렇게 엿을 먹이는 방법도 있다.
***
## 저장에 관하여
***
```
### 영구적으로 손실없이 데이터를 저장 할 수 있다.
## .txt
### 파일 연다
### 1. 읽기
### 2. 쓰기
### 3. 수정
### 파일 닫기
```
***
## .json
```
### 파일 연다 `import json`
### 1. 읽기
### 2. 쓰기
### 3. 수정
### 파일 닫기
```

***
## .csv (Comma Separated Value : 콤마로 구분된 값(들))

```
### 활용 : Excel, 여려 행과 열로 구분된 파일을 사용 할 때 쓴다.
### 엑셀이 무겁기 때문에 많은 데이터를 다룰 때 csv를 사용한다. 때로는 2차원 배열 형식으로도 사용
### 2d-list
```
ex) 
```
[
    [john, ashely, kane],

    [momo, mama, mimi]
]
```
```
### 파일 연다 `import csv`
### 1. 읽기
### 2. 쓰기
  #### csv 는 사용할 때 한 행씩 작업한다고 생각하면 된다.
### 3. 수정
  #### w를 사는경우는 잘 없고 주로 a를 이용하여 사용을 많이한다.
### 파일 닫기
## with를 사용해서 더 간단하게!
***
#### with = open 한 파일을 임시적으로 제어하고,
#### 제어가 끝나면 자동으로 닫아준다.
```
```
  with open('fishes.csv', 'a',encoding="utf-8" ) as f:
        a = csv.writer(f)
        a.writerow([me, you])
```
***
## DataBase
***
```
### DB 열고(connect) => CRUD operation
### 1. 읽기(CREATE)
### 2. 쓰기(READ / RETRIEVE)
### 3. 수정(UPDATE)
### 4. 삭제(DELETE / DESTROY)
### DB 닫기(disconnect)
```

#### `Dictionary(key - value)` + `강력한 메소드 추가` = `object`

#### ORM(Object Relational Mapping)

***
python 에서 뭔가를 만들어보자
```
f = open('파일명','뭘 할지',[인코딩])
f.write('할말')
f.close()
```
뭘 할지 : a(수정) w(쓰기) r(읽기)

```
파이썬의 자료구조는 크게
변수 저장
리스트 - csv
딕셔너리 - json
```