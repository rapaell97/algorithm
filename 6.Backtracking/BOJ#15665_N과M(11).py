def perm(n):
    if n == M:
        print(*ans)
        return

    pre = 0
    for j in range(N):
        if lst[j] != pre:
            pre = lst[j]
            ans[n] = lst[j]
            perm(n+1)

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

ans = [0] * M
V = [0] * N

perm(0)
