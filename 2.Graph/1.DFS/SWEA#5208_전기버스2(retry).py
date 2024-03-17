def dfs(n, B, cnt):
    global ans
    if cnt >= ans:
        return

    if n == M:
        ans = min(ans, cnt)
        return

    if B > 0:
        dfs(n+1, B-1, cnt)

    dfs(n+1, lst[n]-1, cnt+1)


T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    M = lst[0]

    ans = 21e8
    dfs(2, lst[1]-1, 0)
    print(f"#{tc} {ans}")
