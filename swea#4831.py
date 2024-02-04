test = int(input())
for u in range(test):
    k,n,m = map(int,input().split())
    charge = list(map(int,input().split()))
    bus = [0 for _ in range(n+1)]
    for i in range(len(charge)):
        bus[charge[i]] = 1

    i = 0
    cnt = 0
    check = True
    while True:
        i+=k
        if bus[i] == 1:
            cnt += 1
        else:
            check2 = False
            temp = i
            while temp-1 > i-k:
                temp -= 1
                if bus[temp] == 1:
                    check2 = True
                    cnt += 1
                    i = temp
                    break
            if not check2:
                check = False
                break
        if i + k >= n:
            break

    if check:
        print(f"#{u+1} {cnt}")
    else:
        print(f"#{u+1} 0")
