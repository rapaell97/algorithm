def dfs(n, start):
    if n == M:
        print(*ans)
        return

    for j in range(start, N):
        ans[n] = lst[j]
        dfs(n + 1, j)


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = [0] * M
dfs(0, 0)