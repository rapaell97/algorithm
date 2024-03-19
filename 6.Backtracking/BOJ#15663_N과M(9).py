def dfs(n):
    if n == M:
        print(*ans)
        return

    pre = 0
    for j in range(N):
        if arr[j] != pre and V[j] == 0:
            V[j] = 1
            ans[n] = arr[j]
            pre = arr[j]
            dfs(n+1)
            V[j] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

V = [0]*N
ans = [0]*M
dfs(0)