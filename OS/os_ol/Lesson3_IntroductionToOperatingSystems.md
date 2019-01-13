# Lesson 3: P1L2: Introduction to Operating Systems

## Lesson Preview



### What is an Operating system?

####  Simple OS Definition

* A special piece of software that

  * Abstracts and Arbitrates

    Abstract : To simplify what the hardware actually looks like.

    Arbitrate : To manage, To oversee, to control the hardware use.

    => Abstract and Arbitrate mechanism for the various types of hardware components in computer systems

    ```
    Visual Metaphor
    An operating system is like a toy shop manager
    = Directs operational resources
    = Enforce working policies
    = manager mitigates the difficulty of complex tasks
    ----------------------------------------------------------------
    Direct operational resources
    = control use of CPU, memory, peripheral devices => decide how these resources with be allocated to applications
    Enforce working policies
    = Regarding how these resources are used for instance, to control fair access to the shared resources.
    e.g; fair resource access limits to resource usage
    Mitigate difficulty of complex tasks
    = Abstract hardware detials(system call)
    ```



    An operating system is a layer of systems software that:

    - directly has privileged access to the underlying hardware;
    - hides the hardware complexity
    - manages hardware on behalf of one of more applications acording to some predefined policies
    - in addition, it ensures that applications are isolated and protected from one other



### What are key components of an operating system?

OS Element

Abstraction

 * process, thread, file, socket, memory page

Mechanisms

* Create, Schedule, open, write, allocate

Policies

* how these mechanisms will be used to manage the underlying hardware
* least-recently used(LRU), earlisest deadline first

### Design and implementation considerations of operating systems

#### Separation of mechanism 2 policy

* implement flexible mechanisms to support many policies
* e.g) LRU, LFU, random
* Optimize for common case

