import sys
sys.setrecursionlimit(10**6)
def dfs(p,q):
    lst[p][q] = 0
    for j in range(8):
        np = p + di[j]
        nq = q + dk[j]
        if 0<= np <M and 0<= nq <N and visit[np][nq] == 0 and lst[np][nq] == 1:
            visit[p][q] = 1
            dfs(np,nq)

while True:
    N , M = map(int,input().split())
    if N == 0 and M == 0:
        break
    lst = [list(map(int,input().split())) for _ in range(M)]
    di = [-1,-1,-1,0,1,1,1,0]
    dk = [-1,0,1,1,1,0,-1,-1]
    visit = [[0 for _ in range(N)] for _ in range(M)]

    cnt = 0
    for i in range(M):
        for k in range(N):
            if lst[i][k] == 1:
                dfs(i,k)
                cnt += 1
    print(cnt)
