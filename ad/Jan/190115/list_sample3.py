T = int(input())
for t in range(1,T+1):
    a = int(input())
    b = list(map(int, input()))
    c = [0]*10
    c_m = 0
    o = 0
    cp = []
    for i in b:
        c[i] += 1
    for j in range(len(c)):
        if c[j] == max(c):
            cp.append(j)
    if len(cp) > 1:
        c_m = max(cp)
    else :
        c_m = c.index(max(c))
    print(f"#{t} {c_m} {max(c)}")