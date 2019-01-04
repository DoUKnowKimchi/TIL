# 2. System Structure & Program Execution

컴퓨터 시스템에서 하드웨어가 어떻게 동작하는지, 프로그램이 하드웨어 위에서 어떻게 동작하는지.

[ CPU - MEMORY ] COMPUTER =>  [ DISK ] I/O DEVICE

`memory` : CPU의 작업공간
CPU는 매 클럭사이클 마다 메모리에서 인스트럭션(기계어)를 읽어서 실행한다.

`I/O Device` : Disk, keyboard / mouse / printer / monitor  
이를 전담하는 CPU 같은게 있는데 이는 device controller. Disk 내부의 통제는 Disk controller 가 작용함.

device controller도 그들의 작업 공간이 필요한데, 이를 local buffer라 함.

CPU는 매클럭마다 인스트럭션 읽어서 실행, 이를 반복한다. 메모리에서 인스트럭션을 읽고, 실행을 반복.

CPU 안에는 메모리 보다 더빠르면서 저장할 수 있는 registers가 있고, mode bit가 있는데, 이는 이게 운영체제인지, 사용자 프로그램인지 확인.

`interrupt line` : 메모리에 있는 걸 계속 실행하다 보면, I/O에 작업 처리 못함, 이를 해결하기 위해.  
CPU는 MEMORY 하고만 일 한다.  
CPU는 I/O에 직접 접근하지 않고 MEMORY하고만 작업. Disk controller에게 일을 실행 -> 일 하는 동안 local buffer에 저장을 함 -> 그 동안 CPU는 메모리 접근을 계속하면서 인스트럭션 실행.  -> 프로그램에서 I/O 결과가 나오지 않으면 다른 프로그램에게 프로세스를 넘긴다.

만약 무한 루프를 도는 프로그램이라면 계속 CPU를 독점적으로 사용할 수 있음, 그러면 TIME SHARING과 같은 걸 처리 할 수 없음. 그래서 하드웨어에 TIMER라는 것을 가지고 있는데, 프로그램이 CPU를 독점하는 것을 방지한다.  
이는 TIMER에 특정 값을 세팅하고, CPU를 전달해줌. 
이 특정 값이 지나면 TIMER가 CPU에게 알려줌(Timer Interrupt).  
CPU는 인스트럭션 처리 후 Interrupt Line을 확인하고 작업함.

운영체제가 CPU를 얻으면, TIMER에 값을 세팅 후 user program에게 넘겨줌.

사용자 프로그램이 i/o가 필요하면, OS에게 cpu를 넘기고, os가 CPU를 받아서 작업을 처리함.

I/O 작업이 끝나면 키보드 컨트롤러가 CPU에게 인터럽트를 걸고, 인터럽트가 걸리면 CPU가 운영체제에게 옮겨지고, 운영체제가 이를 확인하고 어떤 프로그램의 요청인지 확인한 후 그 프로그램에게 CPU를 전달.(Round Robin)
***
`mode bit` : CPU를 OS가 가지는지, 사용자 프로그램이 가지고 있는지 알려줌

Mode bit : 0 모니터 모드(= 커널 모드, 시스템 모드)  
무슨일이든지 할 수 있게 정의됨(메모리 접근 부터 I/O 접근 까지)  

Mode bit : 1 사용자 모드  
제한된 Instruction만 CPU에서 실행할 수 있게 함(보안상 문제, I/O는 막음)

사용자 프로그램의 잘못된 수행으로 다른 프로그램 및 운영체제에 피해가 가지 않도록 하기 위한 보호 장치.  
Interupt Exception 발생 시 하드웨어가 mode bit을 0으로 바꿈  
사용자 프로그램에게 CPU를 넘기기 전에 mode bit을 1로 셋팅
***
Timer : 특정 프로그램이 CPU 독점을 막기 위해 OS가 사용자 프로그램에게 CPU를 넘겨줄 때 타이머에 특정 값을 할당, 이게 끝나서 0 이 되면 Interupt를 걸어 CPU를 뺏게 sth을 한다.
***
Device Controller  
I/O Device controller : 해당 I/O 장치유형을 관리하는 일종의 작은 CPU  
제어 정보를 위해 control register, status register 를 가짐  
local buffer를 가짐(일종의 data register)

I/O는 실제 device와 local buffer 사이에서 일어남  

Device controller는 I/O가 끝날 경우 Interrupt로 CPU에 사실을 알림.

`device driver(장치구동기)` : OS 코드 중 각 장치별 처리루틴(SOFTWARE)  

`device controller(장치제어기)` : 각 장치를 통제하는 일종의 작은 CPU(HARDWARE)


CPU는 local buffer에도 접근할 수 있는데, local buffer에 있는 정보를 memory에 copy하여 작업한다.

CPU는 Interrupt를 많이 당하는데 빠른 장치가 효율적으로 동작하지 않음. 그래서 DMA controller를 둔다.
***
`DMA Controller(Direct Memory Access)` : 메모리를 CPU도, DMA도 접근할 수 있게 함. 특정 메모리에 동일하게 접근 할 수 있기에, Memory Controller에는 접근 제어에 대한 것 또한 다룬다.  
DMA controller는 중간 중간 I/O interrupt로 local buffer에 있는 내용을 memory로 copy하는게 overhead가 크기 때문에 이를 CPU가 처리하는게 아니라 DMA controller 가 담당하게 함.  
CPU가 interrupt 당하는 빈도가 줄어, 더 효율적으로 작업 할 수 있게 함.
***
CPU는 본인이 실행해야 할 인스트럭션 메모리 주소를 레지스터 중에서 프로그램 카운터(PC)라는 레지스터가 다음번에 어디에 있는 인스트럭션을 실행해야 할지에 대한 주소를 가지고 있음.  
매번 그 인스트럭션만 실행하는게 CPU의 업무.  
I/O를 사용해야 할 경우 Device Driver를 통해 작업을 한다. Device Driver는 Disk안에 펌웨어(인스트럭션 코드)에 의해 controller와 local buffer를 이용해 작업을 한다.

CPU는 매뉴얼 대로 일을 한다. 메뉴얼에 메모리 몇번지에 있는 일을 하라고 정해짐. 그 이후 다음 페이지의 일을 수행함.  
이 CPU의 전체적인 통제를 OS가 한다.
***
모든 입출력 명령은 특권 명령. 사용자 프로그램은 System call(사용자 프로그램이 운영체제의 서비스를 받기 위해 커널의 함수를 호출)을 통해 운영체제에게 I/O 요청 => 소프트웨어 적으로 Interrupt를 건다. 그러면 mode bit이 0이 되서 OS로 CPU가 전달되고, CPU가 이를 해석해서 I/O 작업을 시킨다.(SW Interrupt, Trap)  
일반적인 Interrupt는 하드웨어 인터럽트. 광의는 SW + HW  

OS는 올바른 요청인지 확인하고, 권한 등을 확인 한후 올바른 요청일 경우 I/O 요청을 I/O Controller에게 요청, 이게 시간이 오래걸려 CPU는 다른프로그램에게 전달되고, I/O 작업이 끝나면 HW Interrupt 발생, 다시 그 특정 프로그램에게 CPU가 전달 됨.

그래서 trap이 발생할 시 HW와 SW interrupt 둘다 발생하게 된다.  

그래서 현대의 운영체제는 Interrupt에 의해 구동된다고 이야기 한다.

`인터럽트 벡터` : 해당 인터럽트의 처리 루틴 주소를 가지고 있음  

`인터럽트 처리 루틴(Interrupt Service Routine, Interrupt Handler) `: 해당 인터럽트를 처리하는 커널 함수
***
CPU는 매순간 메모리에 위치한 기계어(인스트럭션)를 읽어서 실행하는데, 그 주소는 Program Counter(PC)라는 레지스터에서 확인하여 실행한다. PC 는 주로 4Byte로, 증가시 4Byte 증가.

기계어 집합 중 jump를 하는것도 있음(주로 순차적으로 실행하나 가끔)

CPU는 아주 빠른 일꾼이라고 생각하면 된다. CPU는 PC register가 가르키는 주소를 읽고 실행. 다음 인스트럭션 실행하기 전 인터럽트가 있는지 확인. 있으면 CPU 제어권이 운영체제에게 넘어가고, OS 커널 함수가 인터럽트 벡터를 확인 후 인터럽트 처리 루틴을 실행한다. 없으면 PC에 나와있는 다음 주소를 따라서 실행한다.

운영체제의 mode bit이 0일 때는 모든 작업을 할 수 있으나, mode bit이 1 일 때는 사용자 프로그램이 CPU 제어권을 가지고 있으므로 한정적인 처리만 가능(보안, 보호 문제 때문에.)  

IO 작업은 mode bit이 0일때만 가능. 따라서 사용자 프로그램은 System call을 통해 작업(trap : SW Interrupt) 바로 점프가 불가능 하기 때문에 의도적으로 Interrupt line setting => CPU는 하던일을 멈추고 CPU 제어권이 사용자 프로그램에서 OS로 이동함  

일반적인 Interrupt 는 HW Interrupt

때때로 SW가 Interrupt를 거는데 이를 Trap이라함.

Trap은 System call과 Exception 두 종류로 구성 됨.Exception : (Devide 0, OS memory access)

***

Timer가 Interrupt를 거는 경우 : 사용자 프로그램이 일방적으로 CPU 독점을 방지하는 것. OS가 CPU를 넘겨줄 때 시간 세팅을 하고 넘겨줌. 할당된 시간이 끝나면 타이머가 CPU에게 Interrupt, CPU 제어권을 뺏고 다른 작업 진행.

***

## 동기식 입출력과 비동기식 입출력

### 동기식 입출력 (Synchronous I/O)
Synchronize : 같이 무엇인가를 맞춤.
I/O 요청후 입출력 작업이 완료한 후에 제어가 사용자 프로그램에게 넘어감  

구현 1
    I/O가 끝날 때 까지 CPU 낭비
    매시점 하나의 I/O 만 일어날 수 있음

구현 2
    I/O가 완료될 때까지 해당 프로그램에게서 CPU를 빼앗음
    I/O 처리를 기다리는 줄에 그 프로그램을 줄 세움
    다른 프로그램에게 CPU를 줌

### 비동기식 입출력 (Asynchronous I/O)
I/O 가 시작된 후 입출력 작업이 끝나기를 기다리지 않고 제어가 사용자 프로그램에 즉시 넘어감

두 경우 모두 I/O 완료는 Interrupt로 알려줌.

***
### DMA(Direct Memory Access)
메모리 접근할 수 있는 장치는 CPU밖에 없었으나, local buffer에서 copy 또는 Memory 에 있는 data를 local buffer로 이동시에도 interrupt가 발생하는데 이게 너무 많아서 CPU에게 과부하가 되고 overhead가 발생하게 된다. 이를 해결하기 위해 DMA controller를 붙여서, DMA controller도 memory에 접근하여, 작은 일들을 DMA에 (특정크기, 블럭, 페이지 not byte)가 쌓이면 DMA가 메모리에 카피 후 어느정도 블럭에 해당하는 I/O가 쌓이면 CPU에게 알려줌. 그러면 CPU가 Interrupt 당하는 빈도가 적어짐.  

Device의 buffer storage의 내용을 메모리에 block 단위로 직접 전송, block 단위로 Interrupt 발생 시킴.

***
서로 다른 입출력 명령어  
인스트럭션에는 메모리만 접근하는게 있고(Memory Address), I/O에 접근 하는것도 있음(Device Address)

IO 주소도 Memory에 연장 주소를 붙여 Memory Mapped I/O에 의해서 메모리 인스트럭션에서 더 효율적으로 접근할 수 도 있음.
***
### 저장장치 계층 구조
Register > Cache Memory > Main Memory [Primary, System Executuable] 

=> CPU Access / Byte  
1clock cycle => 1 instruction(CPU)  
10~100 clock cycle => 1 instruction(Main Memory)  
3~8 lock cycle => 1 instruction(Cache Memory)

** Catching : 기법 copying information into 
faster storage system. 재사용을 목적으로 함. 한번은 밑에서 읽어서 위로 올려야 함. 

Flash Memory > Magnetic Disk> Optical Disk > Magnetic Tape [Secondary]   
Non-excutable / Sector / CPU Non Access

Storage / Speed / Cost / Volatility

***
### 프로그램의 실행(Memory load)
File System => Virtual Memory => Physical Memory / Swap area(Memory의 보조 용도, 연장 공간 사용함.)

Virtual Memory : 각 프로그램마다 가지고 있는 주소 공간.

실행파일 A, 실행파일 B를 실행시 프로세스 A, B의 Address space가 생긴다. code / data / stack 영역으로 구성. => 물리적인 메모리에 적재 시 주소공간이 생겼다가 사라지는데, 이는 당장 필요한 부분만 올리고 나머지는 올리지 않음(메모리 효율성을 위해) => 그렇지 않은 부분은 Swap area에 남겨둠

주소변환 : 메모리 주소변환 계층(Logical => Physical ) (하드웨어의 도움을 받아서 진행된다.)  

### 커널 주소 공간의 내용


|code    | data | stack|
--------------------------
커널 코드   |  PCB(Process Control Block, 프로그램 관리를 위한 커널, 프로그램 마다 하나씩 만들어짐)  / CPU / MEM / DISK | Process A의 커널 스택(프로세스 마다 커널이 생성)
--------------------------
시스템콜, 인터럽트 처리 코드  
자원 관리를 위한 코드  
편리한 서비스 제공을 위한 코드

### 사용자 프로그램이 사용하는 함수

함수(function)
1.  사용자 정의 함수 : 자신이 프로그램에 정의한 함수
2.  라이브러리 함수 : 누가 만들어 놓은 것  
=> 컴파일에서 내 프로그램 안에 포함
3.  커널 함수 : 운영체제 프로그램의 함수, 커널 함수의 호출(System Call을 통해 사용)