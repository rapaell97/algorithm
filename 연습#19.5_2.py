lst = [list(map(int,input().split())) for _ in range(5)]

di = [-1,-1,0,1,1,1,0,-1]
dk = [0,1,1,1,0,-1,-1,-1]
check = True
for i in range(len(lst)):
    for k in range(len(lst[i])):
        d = 0
        if lst[i][k] == 1:
            for j in range(8):
                ni = i + di[d]
                nk = k + dk[d]

                if 0<= ni <len(lst) and 0<= nk <len(lst[i]):
                    if lst[ni][nk] == 1:
                        check = False
                        break
                d += 1
        if not check:
            break
    if not check:
        break

if check:
    print("안정된 상태")
else:
    print("불안정한 상태")