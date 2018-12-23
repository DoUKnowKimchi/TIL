# 우분투 커맨드 정리

## 시스템 종료
***
`poweroff` `shutdown -P now` `halt- p` `init 0`

`-P` 또는 `-p` 옵션은 시스템 종료를 의미한다.

`shutdown -P +10` => 10분 후 종료

`shutdown -r 22:00` => 오후 10시에 재부팅

`shutdown -c` => 예약된 shutdown 취소 (`c =>` cancel)

`shutdown -k +15` => 15분 후에 종료한다고 하지만 실제 종료는 안됨

    root 사용자와 일반 사용자를 구분하려면 프롬프트의 표식을 확인해야 하는데,
    #이면 root 사용자, $면 일반 사용자다.

`reboot` , `shutdown -r now`, `init 6` =>  시스템 재부팅

***
## 가상콘솔

***
 x 윈도 , GUI는 `ctrl` + `alt` + `f7`
 
 가상콘솔은 가상 모니터와 비슷한 개념이며 우분투는 총 7개의 가상 콘솔을 제공한다.

***
## 런레벨(Run Level)
***
 init 명령어 뒤에 붙는 숫자를 런레벨이라고 함. 리눅스는 시스템이 가동되는 방법을 7가지 런 레벨로 나눔.

| Run level | 영문 모드 | 설명 | 비고 |
| ---------  | ------------ |-----|-------|
|0|Power Off |종료모드 | |
|1|Rescue| | 단일 사용자 모드|
|2|Multi-User| | 사용하지 않음|
|3|Multi-User| 텍스트 모드의 다중 사용자 모드||
|4|Multi-User| | 사용하지 않음|
|5|Graphical|그래픽 모드의 다중 사용자 모드| |
|6|Reboot| | |

이는 `cd /lib/systemd/system` 이후 `ls -l runlevel?.target` 으로 확인 할 수 있다.

내가 설치한 Server 와 Client는 부팅 시 자동으로 X 윈도가 시작되므로 Run level 5로 지정.
 
 Server(b) 는 text mode 이므로 run level 이 3번으로 지정된다.
 
 현재 시스템에 설정된 런레벨은 `/lib/systemd/system/default.target`을 확인하면 알 수 있다.

 이 외에도 리눅스 커널에서는 수천개의 명령어가 있으니 외우는건 불가능하고 무의미한 일이지도 모른다. 
 
 그래서 우리는 `man` manual을 사용해야 한다. ex) `man ls`

***
 ## 마운트와 CD/DVD/USB 활용

 ***
 Windows의 경우 마운트라는 개념이 존재하지 않으나
 
  Linux에서는 하드디스크의 파티션, CD/DVD, USB 메모리등을 사용하려면 지정한 위치에 연결해야 한다.

  물리적인 장치를 특정한 위치에 연결시켜 주는 과정을 **마운트** 라고 한다.
  ***
  ## 리눅스 관리자를 위한 명령어
  `dpkg` 와 `apt-get`
  `apt-get`이 나오기 전에는 `dpkg(Debian Package`가 사용되었으나
  `apt-get`은 `dpkg`의 개념과 기능을 포함하기 때문에 `apt-get`을 사용하면 된다.

  `dpkg`가 나온 배경으로 초창기 리눅스는 새로운 프로그램을 다운받는게 꽤 어려워 초보자는 프로그램 설치하는 것도 어려웟다고 한다. 이런점을 개선하여 데비안 리눅스에서 setup.exe와 비슷하게 프로그램을 설치 후 바로 실행할 수 있는 설치 파일을 제작하게 되었는데, 이 설치파일의 확장자가 `*.deb`이며, 이를 `패키지`라고 부른다.
  `deb`파일의 형식은
  ```
  패키지이름_버전-개정번호_아키텍처.deb
  ex)  firefox-gnome-support_22.0+build2-0ubuntu0.12.04.2_amd64.deb
  패키지 파일의 이름은 firefox-gnome-support
  ```
  ### 자주 사용하는 dpkg 명령어 옵션
    * 설치
        - i or --install
    *   삭제
        dpkg -r  (기존에 설치된 패키지 삭제)
        dpkg -P or --purge (기존에 설치된 패키지 삭제 및 설정파일 까지 제거)
    *   조회
        dpkg -l 패키지 이름 (설치된 패키지에 대한 정보 보여줌)
        dpkg -L 패키지 이름 (패키지가 설치한 파일 목록을 보여줌)
    * 아직 설치되지 않은 deb 파일 조회
        dekg --info 패키지파일이름.deb (패키지 파일에 대한 정보를 보여줌)
    
 ### dpkg의 단점
 의존성문제. ubuntu의 기본 프로그램 중 x 윈도상에서 가동되는게 있는데, 단지 CLI로만 작동하는 SW의 경우 이상이 없으나, GUI 의 경우 문제가 발생. 이 문제를 해결한 것이 apt-get 명령어.

***
## apt-get
  dpkg 명령어의 패키지 의존성 문제를 완결하게 해결 해 준다. 

  특정 패키지를 설치할 때 의존성이 있는 패키지를 먼저 설치해주는 명령어

 인터넷으로 알아서 설치해줌. like a npm

 이 저장소의 위치는 /etc/apt/sources.list

### apt-get의 기본 용법
    *   기본 설치 방법
        apt-get -y install 패키지 이름
    *   패키지 목록 업데이트
        apt-get update
    * 삭제
        apt-get remove 패키지 이름
        apt-get purge 패키지 이름
        apt-get autoremove => 사용하지 않는 패키지 모두 지움
    * 내려받은 파일 제거
        apt-get clean or apt-get autoclean => 설치할 때 내려받기한 파일 및 과거의 파일을 제거
    * 의존성 확인 apt-cache
        * 패키지 정보 보기
            apt-cache show 패키지 이름
            apt-cache depends
            apt-cache rdepends => 패키지 역의존성 확인

    * apt-get  의 작동 방식과 설정 파일
        apt-get 명령어와 관련된 설정파일은 /etc/apt/ dir에 있음. 중요한건 sources.list
        `sources.list` : apt-get 명령 실행시 인터넷에서 해당 패키지 파일을 검색하는 네트워크 주소가 들어 있음.
***
## CRON 과 AT
    주기적으로 반복되는 일을 자동으로 실행할 수 있또록 시스템 작업 예약 해놓는 것을 cron. cron과 관련된 데몬(서비스)는 crond 이고 관련파일은 /etc/crontab

    at은 일회성 작업을 예약하는 것.