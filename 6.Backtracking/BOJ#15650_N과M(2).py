def dfs(n, start):
    if n == M:
        print(*ans)
        return

    for j in range(start, N + 1):
        ans[n] = j
        dfs(n + 1, j + 1)

N, M = map(int, input().split())
ans = [0] * M
dfs(0, 1)