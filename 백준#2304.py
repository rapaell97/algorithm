case = int(input())
loc = [list(map(int,input().split())) for _ in range(case)]
N = 0
M = 0

for i in range(case):
    if loc[i][0] > N:
        N = loc[i][0]
    if loc[i][1] > M:
        M = loc[i][1]
lst = [[0 for _ in range(N+2)] for _ in range(M+1)]

for c in range(case):
    for j in range(loc[c][1]):
        lst[j][loc[c][0]] = 1

for i in range(len(lst)):
    for k in range(len(lst[i])):
        if lst[i][k] == 1:
            cnt = 0
            temp_k = k+1
            check = False
            while temp_k < N+2:
                if lst[i][temp_k] == 0:
                    cnt += 1
                if lst[i][temp_k] == 1:
                    check = True
                    break
                temp_k += 1
            if check:
                for j in range(1,cnt+1):
                    lst[i][k+j] = 1
ans = 0
for o in lst:
    for u in o:
        if u == 1:
            ans += 1

print(ans)
