def dfs(i,k):
    global temp
    lst[i][k] = 0
    temp += 1
    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]
        if 0<= ni <N and 0<= nk <N and lst[ni][nk] == 1:
            dfs(ni,nk)
            
N = int(input())
lst = [list(map(int,input())) for _ in range(N)]
di = [-1,0,1,0]
dk = [0,1,0,-1]
ans_lst = list()
ans = 0
temp = 0
for i in range(len(lst)):
    for k in range(len(lst[i])):
        if lst[i][k] == 1:
            temp = 0
            ans+=1
            dfs(i,k)
            ans_lst.append(temp)

print(ans)
ans_lst.sort()
for i in ans_lst:
    print(i)