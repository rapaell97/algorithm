def dfs(n):
    if n == M:
        print(*ans)
        return

    pre = 0
    for j in range(N):
        if arr[j] != pre:
            if n >= 1:
                if arr[j] >= ans[n - 1]:
                    ans[n] = arr[j]
                    pre = arr[j]
                    dfs(n + 1)

            else:
                ans[n] = arr[j]
                pre = arr[j]
                dfs(n + 1)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

ans = [0]*M
dfs(0)