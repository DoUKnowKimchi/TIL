T = int(input())
for t in range(1,T+1):
    b,c = list(map(int, input().split()))
    d = list(map(int,input().split()))
    e = []
    for i in range(b-c+1):
        s_d = d[i:i+c]
        s_d = sum(s_d)
        e.append(s_d)
    print(e)
    max_e = max(e)
    min_e = min(e)
    res = max_e - min_e

    print(f"#{t} {res}")
    