test = int(input())
for u in range(test):
    k, n, m = list(map(int, input().split()))
    charge_lst = list(map(int, input().split()))
    bus_lst = [0 for _ in range(n+1)]

    for i in charge_lst:
        bus_lst[i] = 1

    cnt = 0
    start = 0
    check = True

    while start + k < n:
        if bus_lst[start + k] == 1:
            cnt += 1
            start = start + k
        else:
            moved = False
            for j in range(start + k, start, -1):
                if bus_lst[j] == 1:
                    cnt += 1
                    start = j
                    moved = True
                    break
            if not moved:
                check = False
                break

    if check:
        print(f"#{u+1} {cnt}")
    else:
        print(f"#{u+1} 0")
