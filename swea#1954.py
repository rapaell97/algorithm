test = int(input())
for u in range(test):
    n = int(input())
    lst = [[0 for _ in range(n)] for _ in range(n)]
    di = [0,1,0,-1]
    dk = [1,0,-1,0]
    i,k,d = 0,0,0
    for j in range(1,n**2+1):
        lst[i][k] = j
        ni = i + di[d]
        nk = k + dk[d]
        if 0<= ni <n and 0<= nk <n and lst[ni][nk] == 0:
            i = ni
            k = nk
        else:
            d = (d+1)%4
            i = i + di[d]
            k = k + dk[d]

    for i in lst:
        for k in i:
            print(k,end=' ')
        print()
