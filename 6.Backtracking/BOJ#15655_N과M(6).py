def comb(n, start):
    if n == M:
        print(*ans)
        return

    for j in range(start, N):
        ans[n] = lst[j]
        comb(n + 1, j + 1)

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

ans = [0] * M
comb(0, 0)