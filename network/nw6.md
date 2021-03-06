# 스위치

## 1. 스패닝 트리 알고리즘
스위치나 브리지에서 발생하는 루프를 막아주기 위한 알고리즘  

    스위치나 브리지 구성에서 출발지부터 목적지까지의 경로가 2개 이상 존재할 때 1개의 경로 만을 남겨두고 나머지는 끊었다가, 하나가 이상이 있을 때 끊어두었던 경로를 하나씩 살리는 것.
    Spanning Tree Protocol (STP)
이를 이해하기 위해서는 `BridgeID`와 `Path Cost`를 알아야 한다.  
`BridgeId` : 브리지나 스위치들이 통신할 때 서로를 확인하기 위해 하나씩 가지고 있는 번호  
총 8바이트(64bit)이고, 2 byte는 `Bridge Priority`, 6 byte는 `MAC Address`  

`Bridge Priority` : 0 ~ 65535 까지 값을 갖는데 디폴트는 중간값인 32768 사용. 낮은 값이 더 높은 우선순위를 지님. 등수처럼  

`MAC Address` : 스위치에 고정되어 있는 값  
ex) 32768  / 0260.8c01.1111
=> 8000 0260 8c01 1111  
1000 0000 0000 0000 / 0000 0010 0110 0000 / 1000 1100 0000 0001 / 0001 0001 0001 0001

`Path Cost` : 길을 가는 데 드는 비용. 길이란 장비와 장비가 연결되어 있는 링크  
브리지가얼마나 가까이, 빠른 링크로 연결되어 있는지 알아내기 위한 값

STP를 정의하는 IEEE 802.1D에서 Cost 값 계산할 때 1,000Mbps를 두 장비 사이의 링크 대역폭으로 나눈 값 사용.  

EX) 두 스위치간 10Mbps로 연결되어 있으면 Path Cost = 1000 / 10 = 100
스위치의 대역폭이 상이하고, 나중에 나누었을 경우 소수점이 발생하며 계산이 복잡해지는 문제가 발생하기 때문에, IEEE는 아예 정수값으로 Path CosT를 지정한다.

## 2. STP 핵심 3가지
* 1  네트워크당 하나의 Root Bridge를 가짐(스위치나 브리지로 구성된 하나의 네트워크)  
  `Root Bridge` : STP 수행할 때 기준이 되는 브리지(스위치)
* 2 Root Bridge가 아닌 나머지 모든 브리지는 무조건 하나씩의 루트 포트를 가짐  
  `Root Port` : 루트 브리지에 가장 빨리 갈 수 있는 포트, 루트 브리지 쪽에 가장 가까운 포트.
* 3 세그먼트당 하나의 Designated Port(지정 포트)를 가짐  
  `세그먼트` : 브리지, 스위치 간 서로 연결된 링크. 브리지나 스위치로 연결되어 있을 때 이 세그먼트에서 반드시 한 포트는 Designated Port로 선출되야 한다.

  ** STP에서 Root Port나 Designated Port가 아닌 나머지 모든 포트는 다 막아버린다. 즉, Root Port나 Designated port를 뽑는 이유는 어떤 포트를 살릴지 정하는 것.