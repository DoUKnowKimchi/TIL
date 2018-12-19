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

