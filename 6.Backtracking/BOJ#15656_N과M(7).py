def perm(n):
    if n == M:
        print(*ans)
        return

    for j in range(N):
        ans[n] = lst[j]
        perm(n + 1)

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

ans = [0] * M
perm(0)