def dfs(n, index):
    if n == M:
        print(*ans)
        return

    for i in range(index, N):
        ans.append(lst[i])
        dfs(n+1, i+1)
        ans.pop()

N , M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = list()
dfs(0, 0)