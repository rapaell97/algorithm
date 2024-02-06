m,n = map(int,input().split())
lst = [list(input()) for _ in range(m)]
ans = 64

lstw=[[] for _ in range(8)]
lstb=[[] for _ in range(8)]
for i in range(8):
        if i%2 == 0:
            lstw[i] = ["W","B","W","B","W","B","W","B"]
            lstb[i] = ["B","W","B","W","B","W","B","W"]
        else:
            lstw[i] = ["B","W","B","W","B","W","B","W"]
            lstb[i] = ["W","B","W","B","W","B","W","B"]

for i in range(m-7):
    for k in range(n-7):
        temp_b = 0
        temp_w = 0
        for p in range(8):
            for q in range(8):
                if lst[i+p][k+q] != lstw[p][q]:
                    temp_w += 1
                if lst[i+p][k+q] != lstb[p][q]:
                    temp_b += 1
        ans = min(ans,temp_b,temp_w)

print(ans)
