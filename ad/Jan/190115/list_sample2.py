T = int(input())
for t in range(1, T+1):
    n = 0
    r = 0
    i = 0
    K, N, M = list(map(int, input().split()))
    L = list(map(int, input().split()))
    while not n==N:
        n += K
        while True:
            if n in L:
                r += 1
                break
            else:
                n -= 1    
        # 최소 충전회수 구하기
        # 고려할 사항 : K거리에 정류장이 여러개이면?
    print(f"#{t} {r}")