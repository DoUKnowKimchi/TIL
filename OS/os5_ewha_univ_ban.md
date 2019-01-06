# 5. CPU Scheduling

## CPU and I/O Bursts in Program Execution
![CPU_SCHEDULING_1](/img/cpu_scheduling1.png)

    load store add store read from file => CPU 사용단계(CPU burst)

    wait for I/O   => I/O 사용단계(I/O burst)

    store increment
    index
    write to file

    wait for I/O  
    load store
    add store
    read from file

    wait for I/O

    user와 interact 하는 프로그램의 경우 이렇게 I/O가 많이 발생한다.
    이는 CPU burst 와 I/O burst의 주기가 짧고 빈도가 잦다는 것을 이야기 함.

컴퓨터에는 I/O bound job 과 CPU bound job이 있는데, 일반적으로 I/O bound job의 사용 빈도가 높고, CPU bound job의 빈도는 낮음. 그러나 duration에서 차이가 난다.

그러나 우리는 여러 종류의 job(process) 가 섞여 있는 환경에서 작업하므로 CPU Scheduling이 필요하다.

CPU Scheduling에서 우선순위는 공평성 보다 User 편의성을 더 고려하는데, 사용자가 답답하거나 막막하지 않게 하기 위해 기본적으로 User I/O 관련한 process에게 우선순위를 먼저 준다.

## 프로세스의 특성 분류  
프로세스는 특성에 따라

*  I/O- bound process : many short CPU bursts

* CPU-bound process : few very long CPU bursts

## CPU Scheduler & Dispatcher
* CPU Scheduler : 누구에게 CPU를 줄 것인가?  
Ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고른다.  
OS 안에 존재하는 코드(메소드)

* Dispatcher : CPU의 제어권을 CPU scheduler에 의해 선택된 프로세스에게 넘긴다. ( 이 과정을 context switch 라고 한다.)

* CPU 스케줄링이 필요한 경우는 프로세스에게 다음과 같은 상태 변화가 있는 경우

    1. Running -> Blocked
    2. Running -> Ready
    3. Blocked -> Ready
    4. Terminate

    ** 1,4 에서 스케줄링은 *nonpreemptive*(= 자진 반납) All othere scheduling is *preemptive*(강제 반납)