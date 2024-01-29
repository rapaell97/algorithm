test = int(input())
for u in range(test):
    k,n,m = list(map(int,input().split()))
    charge_lst = list(map(int,input().split()))
    bus_lst = [0 for _ in range(n+1)]

    for i in charge_lst:
        bus_lst[i]=1
    cnt = 0
    start = 0
    for i in range(start,n-k+1):
        check = True
        if bus_lst[start+k] == 1:
            cnt+=1
            start=start+k
        else:
            if 1 in bus_lst[start+k:start:-1]:
                for j in range(start+k,start,-1):
                    if bus_lst[j] == 1:
                        cnt +=1
                        start = j
                        break
            else:
                check = False

        if start+k >= n:
            break
    if check is True:
        print(f"#{u+1} {cnt}")
    else:
        print(f"#{u+1} 0")





