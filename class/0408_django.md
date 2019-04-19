1. zzu.li/install-pyenv

=> pyenv. install 3.6.7

=> pyenv. global 3.6.7

이후 Directory 만들고 여기서 가상환경 설정(작업 Directory) => 다른데서는 접근안되고 여기서만 작업하는 작업환경을 만듬

pyenv virtualenv 3.6.7 insta-view

가상환경을 만들고

요안에 들어가면 이안에서만 새로운 환경이 있는 것 처럼 작업가능

이후 => pyenv local insta-venv

pip install Django==2.1.7

django-admin startproject instagram .(장고-어드민아 => 스타트프로젝트를 하는데 인스타 그램 깔아줘 .(현재위치에!))

// 프로그래머가 된다는건 반복적인 작업들을 최소한으로 하는 것.

개발자들이 사랑받는, 개발자들에게 불편함을 제거하는 것도 좋은 포트폴리오 중에 하나.

## 커밋은 logical한 단위로 쪼개서 한다.

맨 처음부터 무엇을 해 왔는지 commit history만 봐도 작업 이력을 볼 수 있게 한다.

강사님은?

###### 빠티에 있는 커밋 히스토리를 참고한다.

```git
if
.gitignore
README.md
instagram
manage.py
  unstaged = >
commit history를 잘 만드는게 중요하다.

1. 프로젝트를 처음 만들었을 때 
manage.py와 app(instagram)
-m "Instagram 프로젝트 생성 및 instagram 앱 생성"
# commit 규약은 회사마다 다르며, 이는 프로젝트 전에 충분히 이야기 함
가장 중요한 것은, commit history 가지고 협업이 가능한지 가능하지 않은지의 문제이다.
# 어느정도 쪼개고, 어느정도 관리해야 할 지
# git remote가 원격 저장소 관리
git remote add origin(메인 저장소, 기본 이름, 저장소의 이름) URL
git remote -v : remote의 상태를 볼 수 있음.
fetch는 pull의 다른말(fetch + merge = Pull)
```

## 기획 후 새로운 서비스를 만들 때 어떤 과정을 거치는가?

### I 무엇을 하는 서비스 인가?
ex) 사용자가 사진 업로드, Interact 하는 app이다.
### II 사용자가 어떻게 서비스를 활용하는지 정의

ex) 무슨 화면을 보여줄 까? Prototyping with Mock-up
user가 서비스를 봤을 때 어떤 모습으로 보여 줄 지

### III 서비스 안에 어떤 데이터가 들어오고, 관리 할 지

ex) Data Modeling 

"BDD " : Behavior Driven Development

적 기획에

"TDD" : Test Driven Development

적 개발을 하는게 요새 개발 트렌드

***

이제 뭔가를 만들어 보자

python manage.py startapp posts로 post 앱 만들고

settings.py 에 추가

#### git 업로드시 logical 단위는 team과 상의 후 결정

