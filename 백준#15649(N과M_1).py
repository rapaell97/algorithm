def dfs(n):
    if n == M:
        print(*ans)
        return
    for i in range(1,N+1):
        if use[i] == 0:
            use[i] = 1
            ans.append(i)
            dfs(n+1)
            use[i] = 0
            ans.pop()

N , M = map(int,input().split())
use = [0 for _ in range(N+1)]
ans = list()
dfs(0)
