## OSI 7 Layer(Open Systems Interconnection) 7 Layer
***
통신에 관한 국제 표준기구인 International Organization for Standardization(ISO)에서 만든 OSI 7 Layer는 통신이 일어나는 과정을 7 단계로 나누어 표준화하여 효율성을 높이기 위해 사용 되었다.

Application Layer

Presentation Layer

Session Layer

Transport Layer

Network Layer(라우터)

Data Link Layer(스위치, 브리지)

Physical Layer(데이터 케이블, 허브)

    왜 나눴을까?
     1. 데이터의 흐름을 한눈에 볼 수 있다.
     2. 문제를 해결하기 용이하다. Layer를 7 단계로 구분하여 분석 , 평가 할 수 있기 때문.
     3. 여러 회사 장비를 써도 네트워크가 이상 없이 돌아간다. 표준화 되었기 때문에.

***
### Physical Layer
    주로 전기적, 기계적, 기능적인 특성을 이용해서 통신 케이블로 데이터를 전송하게 된다.

    사용되는 통신 단위는 bit, 전기적으로 On, Off 상태

    데이터를 전달 할 뿐 데이터가 무엇이며 에러가 있는지, 효과적인 전달 방법등에 관여하지 않음.

    통신 케이블, 리피터, 허브 등이 있다.
***
### Data Link Layer
    피지컬 레이어를 통하여 송수신되는 정보의 오류와 흐름을 관리하여 안전한 정보의 전달을 수행할 수 있또록 도와줌.
    통신에서의 오류도 찾고 재전송도 하는 기능
    맥어드레스를 가지고 통신 할 수 있음.
    통신 단위 : 프레임
    브리지, 스위치
***
### Network Layer
    데이터를 목적지까지 안전하고 빠르게 전달하는 것.
    경로를 선택, 주소 정하기, 경로에 따라 패킷 전달
    라우터, Layer 3 스위치(라우터의 기능도 수행하는 스위치)
***
### Transport Layer
    플로우 컨트롤과 에러 복구 기능.
    에러 복구를 위해 패킷을 재전송하거나 플로우를 조절해서 데이터가 정상적으로 전송될 수 있도록 함.
    TCP나 UDP

***
## Protocol : 규약 또는 협약. 통신하기 위한 표준 방식.
인터넷을 사용하기 위해 모든 PC는 TCP/IP 프로토콜을 사용해야 한다.

컴퓨터끼리 서로 통신하기 위해 꼭 필요한 서로 간의 통신 규약 또는 통신 방식에 대한 약속.

프로토콜이 같은 것 끼리만 대화, 통신이 가능하다.

### TCP/IP(Transmission Control Protocol / Internet Protocol)
### IPX Protocol
### AppleTalk
