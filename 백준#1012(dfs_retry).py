import sys
sys.setrecursionlimit(10**6)
test = int(input())
for u in range(test):
    m,n,k = map(int,input().split())
    lst = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        lst[b][a] = 1

    dp = [-1,0,1,0]
    dq = [0,1,0,-1]
    def dfs(p,q):
        lst[p][q] = 0
        for j in range(4):
            np = p + dp[j]
            nq = q + dq[j]
            if 0<= np < n and 0<= nq < m and lst[np][nq] == 1:
                dfs(np,nq)

    cnt = 0
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            if lst[i][k] == 1:
                dfs(i,k)
                cnt+=1
    print(cnt)