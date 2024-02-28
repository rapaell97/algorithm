def abc(n, path):
    global cnt
    if n == N:
        if len(path) >= 1 and sum(path) == K:
            cnt += 1
        return

    abc(n + 1, path + [lst[n]])
    abc(n + 1, path)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    cnt = 0
    abc(0, [])

    print(f"#{tc} {cnt}")

