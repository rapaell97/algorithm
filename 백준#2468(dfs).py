import sys
sys.setrecursionlimit(10**6)
def dfs(i,k,safe):
    if i == N and k == N:
        return
    if lst[i][k] >= safe:
        visit[i][k] = 1
        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]
            if 0<= ni <N and 0<= nk <N and visit[ni][nk] == 0 and lst[ni][nk] >= safe:
                dfs(ni,nk,safe)

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
di = [-1,0,1,0]
dk = [0,1,0,-1]
visit = [[0 for _ in range(N)]for _ in range(N)]
ans_lst = list()
for i in range(1,100):
    temp = 0
    for p in range(len(visit)):
        for q in range(len(visit[p])):
            if visit[p][q] == 0 and lst[p][q] >= i:
                dfs(p, q, i)
                temp += 1
    ans_lst.append(temp)
    for p in range(len(visit)):
        for q in range(len(visit[p])):
            visit[p][q] = 0
print(max(ans_lst))


