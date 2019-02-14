T = int(input())
for t in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    L = list(map(int, input().split()))
    r = 0
    n = 0
    while n<N:
        n_b = list(filter(lambda x:x < n+K, L))
        if n >= N - K:
            break
        elif len(n_b) == 0:
            r = 0
            break
        else :
            r += 1
            n = n_b[-1]
            L = L[L.index(n)+1:] 
    print(f"#{t} {r}")