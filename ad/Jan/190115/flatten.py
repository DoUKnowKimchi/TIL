for t in range(1,11):
    n = int(input()) # 횟수
    w = 100 # 가로의 길이
    # 세로의 길이는 1 ~ 1000 이하
    b = list(map(int, input().split()))
    for i in range(n):
        maxim = b.index(max(b))
        mini = b.index(min(b))
        b[maxim] -= 1
        b[mini] += 1
    print(f"#{t} {max(b)-min(b)}")