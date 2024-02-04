test = int(input())
for u in range(test):
    n,m = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(n)]
    di = [-1,0,1,0]
    dk = [0,1,0,-1]
    cnt = 0
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            temp = lst[i][k]
            for j in range(4):
                ni, nk = i, k
                for l in range(lst[i][k]):
                    ni = ni+di[j]
                    nk = nk+dk[j]

                    if 0<= ni <n and 0<= nk <m:
                        temp += lst[ni][nk]

            if temp >= cnt:
                cnt = temp
    print(f"#{u+1} {cnt}")





