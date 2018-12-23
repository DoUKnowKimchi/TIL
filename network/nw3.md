## TCP/IP
***
Application Layer(Telenet, FTP, HTTP, OSI 5 ~ 7)

Transport Layer(TCP,UDP, OSI 4 ~ 5)

Internet Layer(IP, OSI 3)

Network Access Layer(Network Driver, HW, OSI 1 ~ 2)
***
IP주소는 UNIQUE value.
그러나 현재 IPv4가 동나서 UNIQUE ip 값을 사용한다는 것도 옛말.

내부 네트워크에서는 공인되지 않은 IP 주소를 사용하고 인터넷으로 나갈 때만 공인 주소를 가지고 나가는 방식인 NAT(Network Addres Translation)

동일한 IP 주소를 가지고 여러 명이 인터넷에 접속하면서 포트 넘버만 바꾸는 PAT(Port address Translation)

유일한 IP 주소를 사용하기 위해 누군가가 공인된 IP 주소를 관리하고 나눠줘야 하는데 이런 기관이 NIC(Network Information Center)

IP 주소는 32개의 2진수로 만들어짐.

    210.218.150.25
    0010 0001 0000 /  0010 0001 1000 / 0001 0101 0000 / 0000 0010 0101
    2    1    0    /  2    1    8    / 1    5    0    / 0    2    5


## DHCP(Dynamic Host Configuration Protocol)
DHCP 서버는 IP들을 소유하고 있고, DHCP의 클라이언트들이 IP 주소 요청에 따라 

서버서 가지고 있는 IP주소를 동적으로 할당 하는 것.

DHCP  서버 기능은 Window NT나 Novell Netware에 기본으로 포함되었고, 요즘은 라우터에서 이 기능을 제공하기도 한다.

***

