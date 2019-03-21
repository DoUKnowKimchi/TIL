# 190314 Python Django

## 1. MTV (MVC)

## 1) thin controller Fat Model

Views.py 에 있는 action에서 check를 하여 작업해도 되나, 이걸 Model에서 작업하는 것을 권고함 => 뷰에서는 호출에서 확인 값으로만 사용.

예를들어, 단어장을 만들 때, Models에서 단어에 대한 클래스를 만든다음, 메소드로 팰린드롬을 구하는 메소드를 만들고 이를 View에서 호출하여 작업한다.

이는 MTV에서 Urls.py와 views.py에서 작업량이 절대적으로 많아지게 되는데 이런 구조상에서 V가 무거워지면 전반적인 처리속도가 저하되기 때문에 Model을 상대적으로 두껍게 하여 처리 속도를 다루기 위해 이와 같은 로직을 사용한다.

** 파이썬에서 상수 라는 의미가 없기 때문에 사람들이 명시적으로 대문자로 작성하여 이를 상수로 취급하려고 함.

** 사용자가 파일로 올리는 문서들은 MEDIA라고 명명하는 것이 권고됨

```python
# 이는 파일 업로드를 하기 위함
from django.conf.urls.static import static # static
from django.conf import settings # setting 파일에 접근

# DEV모드에서 반드시 사용해야 함
# dev모드는 setting에서 DEBUG True시
# Debug False시 이 아래 배열은 배포가 된 것이므로 빈 배열을 반환한다.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
```



** DB에 사진을 저장한다면 사진을 Binary로 연산 후 저장한다.(인코딩) 이후 요청에 의해 데이터를 가지고 와서 다시 역연산으로(디코딩) 사진으로 연산하는 과정이 필요한데 이 작업이 속도가 제법 걸리기 때문에 서버에 따로 저장을 하는게 더 효율적이다.



** form enctype="multipartform-data"

** Django Admin page에서 created_at과 updated_at이 나오지 않는데 이는 admin.py에서

```python
class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # 개별화면에서 확인 가능
    list_display = ('id', 'content', 'created_at', 'updated_at') # 리스트에서 보여질 컬럼들

admin.site.register(Posting, PostingModelAdmin)
```

요로코롬 하면 된다. readonly_field에 추가를 해주고 이를 register에 인자로 넣어줘야 가능

```
현재 파일 업로드는 리사이징을 하지 않았는데 서버에 올리고 저장하고 다시 제공하는 것 또한 비용이다. 이를 줄이고 효율적으로 처리하는 방법에 대해서도 고려해야함
```

***

```
오늘 깐 것들
pillow
django-imagekit
# django- 인 친구들은 INSTALLED APP에 설정해 줘야 함
```

```python
#이미지 킷(imagekit을 사용해 보자 in sns/models.py)
from django.db import models

#imagekit
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Posting(models.Model):
    content = models.TextField(default='')
    icon = models.CharField(max_length=20, default='')
    # no image ok # media file내부에 posting 파일을 만든다.연월일 기준으로
    # /%Y/%m/%d 파일을 이렇게 나눈다.
    # 이미지 str에는 사진저장위치

    # save as origin
    # image = models.ImageField(blank=True, upload_to='postings/%Y%m%d')

    #resize
    image = ProcessedImageField(
        upload_to="postings/resize/%Y%m%d",
        processors=[ResizeToFit(width=400, upscale=False)],
        format='JPEG'
    )
    created_at = models.DateTimeField(auto_now_add=True) #한번 할당되고 바뀌지 않음
    updated_at = models.DateTimeField(auto_now=True) #변화가 있을 때 마다 기록

    def __str__(self):
        return f'{self.id}: {self.content[:20]}'

```

=> 이 로직 안에서 데이터 베이스 로직에 들어가야 하는 것들이 아닌 경우 make migrations를 안해도 된다. 즉, 스키마와 관련이 있는 것들이 변경 될 경우 make migrations => migrate를 하면 된다.

=> 파일 이름이 같은 경우 중복될 때 장고가 알아서 자연스럽게 랜덤 문자열 만들어줌

=> 원래 그림은 jpeg인데 윈도우가 3글자 확장명을 쓰므로 jpg를 사용한다 마소는 걸러야 제맛

** DuckTyping

다른 타입을 같은 타입처럼. 오리의 특성을 가지고 있다면 오리이던 아니던 중요하지 않다.

리스트 처럼 접근가능하고 이터러블하고 인덱스 접근이 가능하다면 이걸 리스트로 생각하자. 컴퓨터 아키텍쳐, 디자인에서도 많이 사용됨.