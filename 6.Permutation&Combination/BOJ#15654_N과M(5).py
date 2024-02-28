def perm(n):
    if n == M:
        print(*ans)
        return

    for j in range(N):
        if use[j] == 0:
            use[j] = 1
            ans[n] = lst[j]
            perm(n + 1)
            use[j] = 0

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = [0] * M
use = [0] * N

perm(0)