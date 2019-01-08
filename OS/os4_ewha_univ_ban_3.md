# 4. Process Management

## 1. Process Creation
* 부모 프로세스가 자식 프로세스 생성 (복제 생성 - 프로세스의 문맥{Code, Data, Stack}, Instruction (PC register))  
* 프로세스의 트리 형성
* 프로세스 실행시 자원을 필요로 한다(OS로 받고, 자식은 부모와 공유하거나 안하는 경우도 있음)
* 원칙적으로 공유하지 않음(별도의 프로세스 => 경쟁하는 사이)


    공유 : 부모와 자식이 내용이 똑같을 경우 당장 카피 할 필요가 없다.  
     그래서 리눅스나 일부 모델의 경우 가능한 공유할 수 있는건 공유.  
     (일단 카피하지 않고. PC만 복사해서 같은 곳을 가르킴.  
    이후 내용이 달라질 경우의 공유하던 메모리의 일부를 내어주거나 자신만의 공간을 가짐  
    Copy-on-write : COW / write가 발생 했을 때 Copy 하겠다.)  


* 프로세스 실행시 공존하는 모델이 있고, 자식 생성 후 자식 종료 될 때 까지 기다리는(wait, blocked) 모델

***
복제 모델 : 주소 공간(Address space)은 자식은 부모의 공간을 복사함(Binary and OS data)

복제 된 곳에 새로운 프로그램을 올린다.

복제 => 
### 프로세스 생성시
다음과 같은 System Call에 의해 생성되는데 OS에 의해 생성된다.  
(1) fork() : 새로운 프로세스 생성 - 일단 복제  
** A porcess is created by the fork() system call.  
creates a new address space that is a duplicate of the caller



        int main()
        {
            int pid;
            
            pid = fork();  

            #System call로 인해 return value가 다르다. (부모의 경우 자식 process의 PID 양수, 자식의 경우 0)

            if (pid == 0) /* this is child*/
            else if (pid > 0) /* this is parent cuz OS give PID>0
            printf("\n Hello, I am parent!\n")
        }

    fork() 실행시 PC에서 그 이후를 가르키고 있으므로 무한히 실행되지 않음을 기억할 것
(2) exec() => 새로운 프로그램을 메모리에 올림(덮어 씌움) -  

A process can execute a different porgram by the **exec()** system call. - replaces the momory image of the caller with a new program

    int main()
    {
        int pid;
        pid = fork();
        if (pid == 0)
        {
            printf("\n Hello, I am child! Now I'll run date \n"); 
            #exec system call. 새로운 프로그램으로 덮어 씌움.
            이 프로그램의 처음부분 부터 새로 시작하게 된다.
            execlp("/bin/date", "bin/date", (char*)0);
        } 
        # exec 실행시 밑의 코드는 실행 할 수 없음
        else if (pid > 0) printf("\n Hello, I am parent!\n");
    }
***
### 프로세스 종료시
#### wait() 시스템 콜
프로세스 A가 wait() 시스템 콜을 호출하면 커널은 child가 종료될 때 까지 프로세스 A를 sleep 시킨다(block)  

Child process가 종료되면 커널은 프로세스 A를 깨운다(ready)

    main (
        int childPID;

        childPID = fork();

        if (childPID == 0)

        else {
            wait();
        }
    )

(3) 프로세스가 마지막 명령을 수행한 후 os에게 이를 알려줌 (exit)
  *  자식이 부모에게 output data를 보냄(via wait)
  * 프로세스의 각종 자원들이 OS에게 반납됨
  * 프로세스의 종료
    * 자발적 종료 : 마지막 statement 수행 후 exit() 시스템 콜을 통해. 프로그램에 따라 명시적으로 적어주지 않아도 main 함수가 리턴되는 위치에 컴파일러가 넣어줌
    * 비자발적 종료
        * kill ,break등을 친 경우
        * 부모가 자식을 강제 종료
        * 부모가 종료되는 경우 그 전에 자식들이 먼저 종료된다.

(4) 부모 프로세스가 자식의 수행 종료(abort)
  * 자식이 할당 자원의 한계치를 넘어섬
  * 자식에게 할당퇸 태스크가 더이상 존재하지 않음
  * 부모 프로세스가 종료되는 경우
  (원래 자식 프로세스 부터 종료 후 부모가 종료되는게 일반적.)
  * 단계적인 종료
***
## 2. 프로세스간 협력

### 1. 독립적 프로세스(Independent process)  
 프로세스는 각자 주소 공간을 가지고 수행되므로 원칙적으로 하나의 프로세스는 다른 프로세스의 수행에 영향을 미치지 못함

### 2. 협력 프로세스(Cooperating process)  
프로세스 협력 메커니즘을 통해 하나의 프로세스가 다른 프로세스의 수행에 영향을 미칠 수 있음

### 3. 프로세스 간 협력 메커니즘(IPC : Interprocess Communication)
*  메시지를 전달하는 방법(Message passing) : 커널을 통해 메시지 전달(프로세스간 직접 전달은 불가능함)
    *   프로세스 사이에 공유 변수를 사용하지 않고 메시지로 통신하는 시스템
    *  Direct communication : 통신하려는 프로세스의 이름을 ㅁ여시적으로 표시
    *  Indirect Communication : mailbox - 커널에 존재(또는 port)를 통해 메시지를 간접 전달
* 주소 공간을 공유하는 방법(Shared memory) : 서로 다른 프로세스 간에도 일부 주소 공간을 공유하는 shared memory 메커니즘 => System call로 os에게 알린 후 사용 가능.
![sharedMemory](/img/shared_memory.png)

#### thread : 프로세스간 협력은 아니나, thread는 사실상 하나의 프로세스 이므로 thread들 간에는 주소 공간을 공유하므로 협력이 가능하다.