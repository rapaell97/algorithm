def dfs(n, start):
    if n == M:
        print(*ans)
        return
    for i in range(start, N+1):
        ans.append(i)
        dfs(n+1, i)
        ans.pop()

N , M = map(int, input().split())
ans = list()
dfs(0, 1)
