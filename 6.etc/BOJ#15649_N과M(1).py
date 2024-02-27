def per(n):
    if n == M:
        print(*ans)
        return

    for j in range(1, N + 1):
        if use[j] == 0:
            use[j] = 1
            ans[n] = j
            per(n + 1)
            use[j] = 0

N, M = map(int, input().split())
ans = [0] * M
use = [0] * (N + 1)

per(0)
