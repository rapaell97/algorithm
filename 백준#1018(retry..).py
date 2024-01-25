selo,galo = list(map(int,input().split()))
lst = list()

for i in range(selo):
    lst.append(list(input()))

min_cnt = 8*8

lstw=[[] for _ in range(8)]
lstb=[[] for _ in range(8)]
for i in range(8):
        if i%2 == 0:
            lstw[i] = ["W","B","W","B","W","B","W","B"]
            lstb[i] = ["B","W","B","W","B","W","B","W"]
        else:
            lstw[i] = ["B","W","B","W","B","W","B","W"]
            lstb[i] = ["W","B","W","B","W","B","W","B"]

for i in range(selo-7):
    for k in range(galo-7):
        cntb=0
        cntw=0

        for m in range(8):
            for n in range(8):
                if lst[i+m][k+n] != lstw[m][n]:
                    cntw+=1
                if lst[i+m][k+n] != lstb[m][n]:
                    cntb+=1

        min_cnt = min(min_cnt,cntb,cntw)

print(min_cnt)

















