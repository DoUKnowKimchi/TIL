for TCN in range(1, int(input())+1):
    N, K, M = list(map(int, input().split()))
    bus_stop = list(map(int, input().split()))
    charge = 0
    loc = 0
    while loc < K:
        next_bt = list(filter(lambda x: x <= loc + N, bus_stop))
        if loc >= K - N:
            loc = K
        elif len(next_bt) == 0:
            charge = 0
            loc = K
        else:
            charge += 1
            loc = next_bt[-1]
            bus_stop = bus_stop[bus_stop.index(loc)+1:]
    print("#{tcn} {charge}".format(tcn=TCN, charge=charge))