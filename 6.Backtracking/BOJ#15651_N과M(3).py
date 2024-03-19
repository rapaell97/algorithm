def perm(n):
    if n == M:
        print(*ans)
        return

    for j in range(1, N + 1):
        ans[n] = j
        perm(n + 1)

N, M = map(int, input().split())
ans = [0] * M
perm(0)
