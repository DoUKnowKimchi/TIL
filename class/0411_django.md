Complexity => Abstraction (function)

1. 복잡한 것을 어떻게 요약화 할 수 있을까?
2. 이를 어떻게 해야 할까?

Monolithic design

 일원화된 디자인 => Django server, DB, Static file등이 하나의 서버에 들어가 있는 것

장고는 EC2 or EB(Elastic Beanstalk)

DB는 DB:RDS

Static file => 정적파일은 S3(스토리지 서비스, 해당하는 url만 받아서 사용)

cloud front : static file Serving => CDN을 만들어줌(Content Delivery Network)

웹사이트 로드시 무거운 파일들(CSS, JS, Img)을 한번에 서브 하는게 아니라 서버 가운데 노드를 둔다(프록시 서버, 무거운 콘텐츠들을 delivery 함)



파이썬 이미지를 만들기 위해서

pip install pillow

ImageField는 특정 location에 파일을 저장하고, DB에 주소 값을 넣는다.

Form 태그는 원래 Text 기반의 작은 파일들을 보내는 거였는데, 사진이나 영상의 경우 인코딩 타입을 정해줘야 한다. 다른 문서와는 다르게. 파일은 용량이 크기 때문에 문서를 보내는 것과 사뭇 다르다. 

그래서 form 태그에 attr로 enctype="multipart/form-data"

1. 어떻게 업로드 할 것이며
2. 어떻게 받을 것인가
   * 사진이나 영상은 media / ~.확장자 형식으로 만들어 줘야 함
   * 이를 해주기 위해 settings.py에 어디에 저장되는지 이야기 해줘야 함.
   * settings.py 에 media_root와 meida_url 설정
3. static() : 통과 시키고자 하는 url(media_url), 실제 저장 장소(media_root)
   이 `static` 함수는 `from django.conf.urls.static`에서 `import static`한다
4. 파일 은닉화 : 경로를 찾으려고 할 때 직접적인 url 접근이 아니라 다른 요약된 함수, 객체 를 통해서 접근하게 함 => app이 방대, 관리 할 때 파일 경로가 바뀌면 하나하나 다 바꿔줘야 하는데 이는 정말 어렵고 힘들다.
   함수 내부가 바꾸면 함수를 가지고 활용했던 모든 코드들을 관리 하지 않아도 되기 때문에.
   그래서 `from django.conf import settings`에서 가지고 온다
   이 `conf`는 `settings.py` 뿐만 아니라 수 많은 다양한 환경 설정이 안에 존재하게 된다.
5. 즉 다음과 같이 쓰면된다.
   `urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)`
6. Position argument, keyword_argument(어떤 url 넣고, 어디로 보내줘야 할지)
7. document_root =settings.MEDIA_ROOT 이게 현재 서버주소이고, 외부 서버를 이용한다고 하면 외부 서버 주소를 MEDIA_ROOT에 입력해주면 된다.