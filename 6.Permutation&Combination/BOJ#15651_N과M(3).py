def dfs(n):
    if n == M:
        print(*ans)
        return

    for i in range(1, N+1):
        ans.append(i)
        dfs(n+1)
        ans.pop()
N , M = map(int, input().split())
ans = list()
dfs(0)
