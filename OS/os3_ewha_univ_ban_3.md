# Chapter 3 Process

Process is a program in execution(실행중인 프로그램)

프로세스의 문맥(Context)  
특정 시점을 봤을 때 어디까지 수행했고, 주소 공간을 만들고 CPU를 잡게되면 PC가 어디를 작업하고, 기계어를 읽어 처리하고 레지스터에 저장하거나 메모리에 저장.  

어느 시점에 어디까지 와 있는가를 규명할 때 필요한게 프로세스의 문맥  

 => PC가 어디를 가르키는가?  
  메모리에 어떤 내용을 담고 있는가?(함수 실행시 스텍에 뭘 쌓였는지, data 영역에 변수의 값은 얼마이며, 레지스터에 어떤 값을 넣어놓고 어떤 인스트럭션 까지 수행했는가)
*   CPU 수행 상태를 나타내는 하드웨어 문맥
    *   Program
    *   각종 Register(어떤 값을 가지고 있는지)
    * PC가 어떤 걸 가르키고 있는지
*   프로세스의 주소 공간(메모리와 관련)
    *  CODE
    *  DATA
    *  STACK
*   프로세스 관련 커널 자료 구조
    *   운영체제가 프로세스 관리를 함. 프로세스가 실행될 때 마다 운영체제는 이를 관리하기 위해 데이터 영역에 PCB라는 영역을 하나씩 두고 CPU와 MEMORY 할당 및 감시 관리를 함
    *   PCB(Process Control Block)
    *   Kernel stack(어떤 내용을 쌓고 있는지)

=> 이래야 어떤 문맥에 있는지 규명 가능하다.

프로그램 하나만 돌아가면 알 필요 없지만, TSS와 MP 때문에 다양하고 복잡한 작업을 하기 때문에, 문맥을 알지 않으면 CPU 사용시 초기화 되는 문제가 발생. 이를 해결하기 위해 이 내용들이 나옴
***
## 프로세스의 상태
프로세스는 `상태(State)`가 변경되며 수행된다
*   Running : CPU를 잡고 Instruction을 수행중인 상태
*   Ready : CPU를 기다리는 상태(다른조건은 다 만족하고=> 물리적인 메모리에 올라가 있음)
*   Blocked (wait, sleep) : CPU를 주어도 당장 Instruction을 수행할 수 없는 상태.
    *   오래 걸리는 IO 작업을 기다리는 상태
    *   Process 자신이 요청한 event가 만족되지 않아 대기하고 있는 상태.

`New` : 프로세스가 생성중인 상태  
`Terminated` : 수행(execution)이 끝난 상태.(종료 중, 종료가 되면 프로세스가 아님)
***
new => admitted => ready(in memory) => scheduler dispatch => running => exit => terminated

new => admitted => ready(in memory) => scheduler dispatch => running => exit => I/O or event wait => waiting(blocked) => I/O or event completion => ready

new => admitted => ready(in memory) => scheduler dispatch => running => Timer(interrupt) => ready

![프로세스의 상태](/img/process_state.png)

    All of OS repository's contents is made by  EWHA WOMANS UNIVERSITY KOCW LECTURE 'Operating System', professor 'Bahn Hyo Gyeong'

Queue : 본인의 데이터 영역에 data structure 로 quere를 만들고 여기에서 작업 할 내용들을 쌓아서 순차적으로 처리 한다.
***
Process Control Block(PCB)  
운영체제가 각 프로세스를 관리하기 위해 프로세스당 유지하는 정보  
다음의 구성 요소를 가진다(구조체로 유지)
*   (1) OS가 관리상 사용하는 정보  
    *   Process state, Process ID
    *   Scheduling information, priority  
    Round Robin 처럼 그림이 작성 됬으나, 위에 둘을 따져서 효율적으로 작업 처리
*   (2) CPU 수행 관련 하드웨어 값  
    *   Program counter, registers  
*   (3) 메모리 관련  
    *   Code, Stack, Data의 위치 정보
*   (4) 파일 관련  
    * Open file descriptors(오픈하고 있는 파일이 무엇인가)

![PCB](/img/pcb.png)
***
## 문맥 교환(Context Switch) **
![문맥 교환](/img/context_switch.png)  
짧은 시간 간격으로 CPU를 번갈아 가며 씀. CPU를 뺏길 때 문맥을 기억했다가 다시 얻었을 때 그 문맥 이후 부터 작업.

Register에 있는 값과 PC 의 값, Memory map을 프로세스 PCB에 Save 함

CPU를 한 프로세스에서 다른 프로세스로 넘겨주는 과정

** Memory Map : 메모리에 대한 위치 정보

CPU가 다른 프로세스에게 넘어갈 때 운영체제는 다음을 수행

    CPU를 내어주는 프로세스의 상태를 그 프로세스의 PCB에 저장

    CPU를 새롭게 얻는 프로세스의 상태를 PCB에서 읽어옴

    커널 data stack에 프로세스 마다 가지고 있는 PCB가 존재.

![문맥교환](/img/context_switch2.png)

context switch 는 프로세스에서 프로세스로 넘어가는 것. 프로세스에서 OS로 가는걸 문맥 교환이라고 하는게 아님.  
프로세스 => OS => 다른 프로세스면 문맥 교환이 맞으나 프로세스 => OS => 그 프로세스 면 문맥 교환이 아님.(문맥에 대한 저장이 약간은 되야하나, 다른 프로세스로 넘어가는 것 보다 Overhead가 적은데 이는 Cache memory에 저장한다. 만약 프로세스에서 다른 프로세스로 넘어가면 cache memory flush가 생기기 때문에 상당한 overhead가 발생한다.)

***
## 프로세스를 관리하기 위한 Queue

*   Job queue : 현재 시스템 내에 있는 모든 프로세스의 집합

*   Ready queue : 현재 메모리 내에 있으면서 CPU를 잡아서 실행되기를 기다리는 프로세스의 집합

*   Device queues : I/O Device의 처리를 기다리는 프로세스의 집합

프로세스들은 각 큐들을 오가며 수행된다.

![process queue](/img/process_queue.png)

![process_scheduling_queue](/img/process_scheduling_queue.png)

***
## Scheduler
순서를 정해주는 것.  자원 별로 시간 할당, 작업 순서등
*   Long-Term-Scheduler(장기 스케쥴러, Job Scheduler)
    *   Memory를 어떤 프로그램에게 할당할 지
    *   프로세스가 Memory에 올라가는 것을 Admit 하는 것.
    *   시작 프로세스 중 어떤 것들을 ready quere로 보낼지 결정  
    * 프로세스에 memory를 주는 문제
    *   degree of MultiProgramming을 제어(메모리에 올라가는 프로그램의 수 제어)
    *   Time sharing system에는 보통 장기 스케쥴러 없음(무조건 ready state)

*   Short-Term-Scheduler( 단기 스케줄러 or CPU Scheduler)  
    *   짧은 시간 단위로 스케쥴링이 이루어짐
    *   충분히 빨라야 함(millisecond)
    *   어떤 프로세스를 다음번에 running 시킬지 결정
    *   프로세스에 cpu를 주는 문제

*   Medium-term-scheduler (중기 스케줄러 or Swapper)
    * 메모리가 가득 차게 되면 여유 공간 마련을 위해 몇몇 프로세스를 통째로 메모리에서 디스크로 쫒아냄
    *   프로세스에게서 Memory를 뺏는 문제
    *   degree of MultiProgramming 제어
    *   대부분의 PC는 중기 스케줄러로 스케줄링 작업을 한다.

현대 운영체제에서 프로세스의 상태에서 하나가 더 추가 됬는데, 그게 바로 Suspended (Stopped)

`Suspended` : 외부적인 이유로 프로세스의 수행이 정지된 상태. 프로세스는 통째로 디스크에 swap out 된다  

ex) 사용자가 프로그램을 일시 정지시킨 경우  , 시스템이 여러 이유로 프로세스를 잠시 중단시킴(메모리에 너무 많은 프로세스가 올라와 있을 때)

** Blocked 와 Suspended의 차이는  
`Blocked` : 자신이 요청한 `event`가 만족되면 `Ready`  

`Suspended` : 외부(중기 스케줄러)에서 `Resume`해 주어야 `Active`

***
![프로세스 상태도](/img/process_state_pic.png)
***
## Thread
A thread(or lightweight process) is a basic unit of CPU utilization

![PCB with thread](/img/pcb_with_thread.png)
프로세스는 하나만 띄워놓고 PC만 여러 개 두어서(cpu 수행 단위만 여러개 띄워넣는거, MEMORY register value)
***

Thread : 프로세서 하나에서 공유할 수 있는 것들을 공유하며 스택 및 몇몇 개는 따로 가지고 있음. 사진 참조

![스레드](/img/thread.png)  


Thread의 구성  
(스레드간 독립적으로 가짐)  
*   PC
*   register set(register value)
*   stack space

Thread가 동료 thread와 공유하는 부분(=task) 여러개의 스레드에 하나의 task를 가짐.
*   code section
*   data section
*   OS resources

** 전통적인 개념의 heavyweight process 는 하나의 thread를 가지고 있는 task로 볼 수 있음.

### Thread 사용 장점
    다중 thread로 구성된 task 구조에서 하나의 server thread가 blocked(waiting) 상태인 동안 동일한 task 내의 다른 thread가 실행(running) 되어 빠른 처리 가능

    동일한 일을 수행하는 다중 스레드가 협력하여 높은 처리율(throughput)과 성능 향상을 얻을 수 있음 => 웹브라우저 창을 많이 띄워넣었을 때 각 창마다 프로세스로 작업 할 경우 낭비가 크므로, 쓰레드로 작업하면 효율성을 더 높일 수 있다.

    CPU가 많은 컴퓨터의 경우 병렬성을 높일 수 있음

![Thread](/img/thread_img.png)

![SingleAndMultiThreadedProcesses](/img/single_multi_threaded.png)

### Benefits of Threads

    Responsiveness(응답성)
        Multi-threaded Web -> if one thread is blocked (eg network) another thread continues (eg display)
        -> web open시, loading 전 모든 sources 들이 block 되면 user가 답답함 => 이를 위해서 html 부터 rendering 하는 것.

    Resource Sharing(자원공유)
        n threads can share binary code, data, resource of the process 

    Economy
        Creating & CPU switching thread (rather than a process). use less cpu. make overhead lower than CPU switching

    Utlization of MP (MultiProcessing)Architectures
        each thread may be running in arallel on a different processor

***
## Implementation of Threads
***
Some are supported by kernel => kernel Threads  
(eg Windows, Solaris, UNIX)  
스레드가 여러개 있는 사실을 OS가 알고 있음.

Others are supported by library => User Threads  
user program이 thread를 관리한다. 커널이 모르고 있고, 일반적인 프로세스로 알고 있음.

Some are real-time threads : Real time 기능을 지원하는 threads