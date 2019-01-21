# 2019/01/21

***



## 배열2 => 2차원 배열

### 2차원 배열의 선언

#

***



### 부분집합

***



부분집합의 개수는 2^n가 된다.

* for 문을 많이 작성하면 모든 요소를 다 구할 수 있으나 그 깊이가 너무 깊어짐
* 그러므로 재귀 함수( 백트래킹)을 활용하기도 함.

```py
bit = [0,0,0,0]
for i in range(2) :
	bit[0] = i
	for j in range(2) :
		bit[1] = j
		for k in range(2) :
			bit[2] = k
			for l in range(2) :
				bit[3] = l
				print(bit)
```



### 비트연산자

우리가 숫자를 표현 할 때 int는 4byte => 32bit

맨처음 bit는 부호를 표현한다.

bit 연산자에는 & , | , << , >> 이 존재하는데

```markdown
& | 1	|0|
-----------
1| 1	|0|
-----------
0| 0	|0|
| | 1	| 0|
------------
1 | 1	| 1 |
-------------
0 | 1	| 0 |
-------------
```

```python
arr = [-3,3,-9,6,7,-6,1,5,4,-2]
sum = cnt = 0

for i in range(1, 1<< len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j): sum += arr[j]
            
    if sum == 0:
        cnt += 1
        print('%d : ' %cnt, end= " ")
        for j in range(len(arr)):
            if i& (1 << j):
                print(arr[j], end= " ")
        print()
```

### 검색

***

* 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
* 목적하는 탐색 키를 가진 항목을 찾는 것 ( 탐색 키 : 자료를 구별하여 인식할 수 있는 키)
* 검색의 종류 : 순차 검색(n), 이진 검색(logN), 해쉬

#### 순차검색

* 정렬 되지 않았을 경우

  * 첫 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾음
  * 키  값이 동일한 원소를 찾으면 그 원소의 인덱스 반환
  * 자료구조의 마지막에 이를 때까지 대상을 찾지 못하면 검색 실패

  ```python
  def sequentialSearch(a, n, key)
  	i <- 0
      while i<n and a[i]!=key :
          i <- i+1
      if i<n : return i
      else : return -1
  ```

  

* 정렬 되었을 경우

  * 정렬 되어 있으므로 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어듬

```python
def sequentialSearch2(a, n, key):
    i = 0
    while i<n and a[i]<key :
        i += 1
        if i<n and a[i] = key : return i
        else : return -1
```



#### 이진검색

* 자료의 가운데 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법 : 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로 검색 범위를 반으로 줄여가며 보다 빠르게 검색을 수행
* 이진 검색을 하기 위해서는 자료가 정렬 된 상태여야 함
* 검색과정
  1. 자료의 중앙에 있는 원소를 고른다
  2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다
  3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해 새로 검색 수행, 크다면 자료의 오른쪽 반에 대해 새로 검색 수행
  4. 찾고자 하는 값을 찾을 때 까지 반복

```python
def binarySearch(a, key):
    start = 0
    end = length(a)-1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            return true
        elif a[middle] > key:
            end = middle -1
        else : start = middle + 1
     return false:
```

```python
def binarySearch2(a, low, high, key) :
    if low > high :
        return False
    else :
        middle = (low + high) // 2
        if key == a[middle]:
            return Treu
        elif key < a[middle]:
            return binarySearch(a, low, middle-1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle+1, high, key)
        #범위가 줄고 똑같은 일 반복일 경우 재귀로 작성이 가능하다.
```

#### 셀렉션 알고리즘

```python
def select(list,k):
    for i in range(0, k):
        minIndex = i
        for j in range(i+1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
      return list[k-1]
```

