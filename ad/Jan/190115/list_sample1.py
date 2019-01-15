a = int(input())
for i in range(1, a+1):
    b = int(input())
    c = list(map(int, input().split()))
    m_c, min_c = max(c),min(c)
    print(f"#{i} {m_c - min_c}")