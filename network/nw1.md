# 1. 네트워크 기초
## 네트워크의 종류
*   인터넷(Internet) : 네트워크를 여러 개 묶어놓은네트워크 연합
  
    공통의 프로토콜 사용. (TCP/IP)
*   인트라넷(Intranet) : 로컬 인터넷. 그 지역에서만 사용.
*   엑스트라넷(Extranet) : 인트라넷 + 허용된 외부 로컬 까지 사용가능.
***
## WAN과 LAN
*   WAN(Wide Area Network) :  멀리 떨어진 지역을 서로 연결하는 네트워크 구축
*   LAN(Local Area Network) : 어느 한정된 공간에서 NW 구성.
*   네트워킹 구성은 LAN 과 WAN 의 공존.

## 이더넷(Ethernet) : 네트워킹의 한 방식.
네트워크를 만드는 방법 중하나.

### CSMA/CD (Carrier Sense Multiple Access / Collision Detection) 이라는 프로토콜을 사용해서 통신.
*   CA 
  
    1. 이더넷 환경에서 통신 하고 싶은 PC 나 Server 는 NW상 통신이 일어나는지 확인(이를 Carrier라 함). 
    2. NW상 나타나는 신호가 있는지 확인한다.(Carrier Sense)
    3. 캐리어가 감지되면 잠시 대기한다.
    4. NW상 통신이 사라지면 데이터를 NW에 실어서 통신한다.
*   MA

    1.  데이터 통신이 이루어 지지 않을 때, 다른 두 PC나 서버가 동시에 데이터를 보낼 경우 충돌(Collision이 일어남.) 이 경우를 Multiple Access라고 한다.
    2.  두개 이상의 장비들이 데이터를 동시에 보내려다 부딪히는 경우를 충돌이 났다(Collision) 이라 하며, 이를 점검하는 것을 Collision Detection이라 한다. 
    3.  Collision이 발생한 경우 데이터는 잠시 대기후 재 전송하는 방식으로 통신하게 된다.

## 토큰링(TokenRing) : 네트워킹의 또 다른 한방식
네트워크에서 토큰을 가진 오직 한 장비만 데이터 전송.

데이터를 전송하고 나면 다음 장비에게 토큰을 건내준다.
### 장점
* Collision이 발생하지 않음
* 성능 예측 용이

### 단점
* 대기시간이 길다
* 그러므로 속도가 이더넷보다 느리다.