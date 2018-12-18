# Python Chatbot Day 1

1일차파이썬 기반 챗봇 만들기

[챗봇 플랫폼](https://s1.py.hphk.io)

![](https://www.python.org/static/opengraph-icon-200x200.png)





## 1. 기초 문법

### (1) 저장

#### 1. 개념

 파이썬은 **Dynamic typing language ** => 자료형 정의가 필요 없다.

1. 숫자

   ```python
   greeting = 'hello world'
   ```

2. 글자

3. boolean

#### 2. 실습

```python
# 변수 활용하기
greeting = '안녕하십니까 행님  ⎛⎝⎛° ͜ʖ°⎞⎠⎞ '
print(greeting, '인사 오지게 박습니다.\n')
for x in range(5):
  print(greeting, '\n')
```



## 2. 개발 계명(Development Commandments)

#### (1) 브라우저는 Chrome 이다

#### (2) 문서는 마크다운(.md) 이다.

 ##### 	github에서 README.md 클릭 후 raw 에서 사용법을 볼 수 있다.

#### (3) 교과서는 공식문서 & 내가 정리한 마크다운이다.



# 3.  자료구조

#### (1) List

 순서에 기반한 인덱스를 활용

#### (2) Dictionary

 Key - Value mapping, Hash라고도 불린다. 자바스크립트 Object 와 유사함.

#### (3) Tuple, Set  등

  위에 두 자료구조에 비해 사용 빈도가 낮음.





# 4. 조건문

### 기본중의 기본. 연습으로 알아보자.

```python
import requests
from bs4 import BeautifulSoup

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={}&sidoName=서울&pageNo=3'.format(key)
response = requests.get(url).text
soup = BeautifulSoup(response, 'xml')
gn = soup('item')[7]
location = gn.stationName.text
time = gn.dataTime.text
dust = int(gn.pm10Value.text)

print('{0} 기준: 서울시 {1}의 미세먼지 농도는 {2} 입니다.'.format(time, location, dust))
print('*********************')
if dust>151:
  print('미세먼지 매우 나쁨')
elif dust>80:
  print('미세먼지 나쁨')
elif dust>30:
  print('미세먼지 보통')
else :
  print('미세먼지 없는 좋은날')
print('*********************')
# 미세먼지 농도가 좋은지 나쁜지 매우나쁜지 혹은 보통인지 출력할 것
```

`파이썬은 다른 언어와 다르게 스위치문이 존재하지 않음을 알아 둘 것`



# 5. 반복

 시작조건과 종료조건을 표현하지 않으면 무한 반복.

파이썬에서 while문은 거의 쓰지 않는데, while 보다 for 문을 더 많이 쓴다(물론, 다른 언어도 그러하다.)

`iteration`  한번씩만 돌면서 뭔가를 하고 종료하려고 할 때.

더 많이 사용하는건 `for` 와 `for x in range(n)`

`for`는 반복 보다는 `iteration`과 유사하다. 정해진 범위 안에서 계속.

``` python
dust = [59, 24, 102]
for i in dust:
    print(i)
#i 대신 다른 이름이 주어져도 된다. 임시 변수와 같은 것.
#출력은 순차적으로 59, 24, 102가 나온다. 
```



`while True`  : 조건이 `True` 일 때까지 반복적으로 실행되기에 종료조건이 반드시 필요.

#### Open Source()

 함수는 포장이다. x를 넣어서 특정 기능을 통해 y가 나오는 것.

 무엇을 배울 때 어떤 것이 input이 되고 어떤 것이 output이 되는지

 요새 프로그래밍에서 중요한게 Abstract. 이걸 어떻게 programming(Abstraction 할지)

 이것의 정수가 Function.

#### API (application Programming Interface 응용 프로그램 프로그래밍 인터페이스)

> 1. 프로그래밍이 가능한 인터페이스.​ 통로가 프로그래밍을 통해 가야 함. 프로그래밍으로 조작할 수 있게 열어 둔 통로가 API. 모든 서비스 / 제품이 API 형태로 자신들의 interface를 열어두기 때문에 코딩과 프로그래밍의 중요성이 더욱 커지고 있다.
> 2. 정보에 접근하고, 사무 자동화를 위해서.
> 3. 회사와 회사 간 정보의 교류, 소프트웨어를 사용하기 위해 (OAuth)
> 4. 서비스들간의 대화 방식
>
>

`interface`  텔레비전 리모콘의 버튼들과 같은 것.



# 6. 웹(WEB)에서의 커뮤니케이션 방식

### 요청(request) 과 응답(response)



# 7. OOP란?

세상을 주어.동사로 해석하는 것

절차지향적 프로그래밍은 한 스트림으로 쭉 프로그래밍 하는데 HW, SW가 점점 더 복잡해 짐으로 인해서 이를 구분해야 할 필요성을 느끼고, 개발 편의성을 위해 나타나게 됨.

# 8. 웹크롤링

```python
# kospi 정보 스크랩

import requests
import bs4

url="https://finance.naver.com/"

response = requests.get(url).text
doc = bs4.BeautifulSoup(response, 'html.parser')

result1 = doc.select_one('#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num')
result2 = doc.select_one('#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num2')
result3 = doc.select_one('#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num3')
print('*********************************************************')
print('코스피지수  ',result1.text, '  증가포인트  ',result2.text, '  증가율', result3.text)
print('*********************************************************')
```



# 9. 파일 입출력 / 편집

```python
import os

os.listdir('.')

os.chdir(r'./li/SSAFY지원자')

os.listdir('.')

os.getcwd()

fileList=os.listdir('.')

for i in fileList:
    os.rename(i, 'ssafy_'+i)
```

import os는 python 에서 os를 컨트롤 하기 위한 모듈임.

`os.chdir()`: cd : change directory의 약자. 매개변수로 경로가 필요함.

`os.listdir()`: ls -al 처럼 현재 디렉토리에 존재하는 파일을 확인

`os.getcwd()`: 현재 디렉토리의 위치를 확인하는 명령어.

`os.rename()`: 매개변수 : `os.rename(파일의이름,바꿀이름)`