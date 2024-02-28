def perm(n, start):
    if n == M:
        print(*ans)
        return

    for j in range(start, N + 1):
        ans[n] = j
        perm(n + 1, j)

N, M = map(int, input().split())
ans = [0] * M
perm(0, 1)